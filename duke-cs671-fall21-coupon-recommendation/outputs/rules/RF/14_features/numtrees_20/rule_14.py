def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Bar", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[9]<=1.0:
		# {"feature": "Coupon", "instances": 35, "metric_value": 0.9852, "depth": 2}
		if obj[2]>0:
			# {"feature": "Passanger", "instances": 29, "metric_value": 0.9991, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Income", "instances": 21, "metric_value": 0.9852, "depth": 4}
				if obj[8]>1:
					# {"feature": "Occupation", "instances": 18, "metric_value": 1.0, "depth": 5}
					if obj[7]>6:
						# {"feature": "Distance", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[13]<=2:
							# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[10]>0.0:
								# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[1]>0:
									# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[11]>1.0:
										return 'True'
									elif obj[11]<=1.0:
										return 'False'
									else: return 'False'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							elif obj[10]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[13]>2:
							return 'False'
						else: return 'False'
					elif obj[7]<=6:
						# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Coffeehouse", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[10]<=0.0:
								return 'False'
							elif obj[10]>0.0:
								return 'True'
							else: return 'True'
						elif obj[6]>0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[8]<=1:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Income", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[8]<=4:
					return 'True'
				elif obj[8]>4:
					# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=0:
						return 'False'
					elif obj[5]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[9]>1.0:
		# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[11]>0.0:
			# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[10]<=3.0:
				return 'True'
			elif obj[10]>3.0:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>2:
					return 'True'
				elif obj[1]<=2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[11]<=0.0:
			# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1]>3:
				return 'False'
			elif obj[1]<=3:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'

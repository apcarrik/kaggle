def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[2]>1:
		# {"feature": "Occupation", "instances": 30, "metric_value": 0.8366, "depth": 2}
		if obj[7]>2:
			# {"feature": "Income", "instances": 23, "metric_value": 0.9321, "depth": 3}
			if obj[8]<=6:
				# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9911, "depth": 4}
				if obj[11]>0.0:
					# {"feature": "Passanger", "instances": 15, "metric_value": 0.9968, "depth": 5}
					if obj[0]>1:
						# {"feature": "Age", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[4]>1:
							# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]>0:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[1]>2:
									# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[6]<=0:
										return 'True'
									elif obj[6]>0:
										return 'False'
									else: return 'False'
								elif obj[1]<=2:
									return 'True'
								else: return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[4]<=1:
							return 'True'
						else: return 'True'
					elif obj[0]<=1:
						# {"feature": "Bar", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[9]<=1.0:
							return 'False'
						elif obj[9]>1.0:
							# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[10]<=2.0:
								return 'True'
							elif obj[10]>2.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[11]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[8]>6:
				return 'True'
			else: return 'True'
		elif obj[7]<=2:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 21, "metric_value": 0.9183, "depth": 2}
		if obj[9]<=1.0:
			# {"feature": "Education", "instances": 16, "metric_value": 0.6962, "depth": 3}
			if obj[6]<=3:
				# {"feature": "Time", "instances": 15, "metric_value": 0.5665, "depth": 4}
				if obj[1]<=3:
					return 'False'
				elif obj[1]>3:
					# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[4]>2:
						return 'True'
					elif obj[4]<=2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[6]>3:
				return 'True'
			else: return 'True'
		elif obj[9]>1.0:
			# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[6]<=3:
				return 'True'
			elif obj[6]>3:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'

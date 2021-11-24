def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Coffeehouse", "instances": 36, "metric_value": 0.888, "depth": 2}
		if obj[10]<=2.0:
			# {"feature": "Education", "instances": 25, "metric_value": 0.6343, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Occupation", "instances": 22, "metric_value": 0.4395, "depth": 4}
				if obj[7]>4:
					return 'True'
				elif obj[7]<=4:
					# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[11]<=1.0:
						# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[1]>1:
								# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[8]>4:
									return 'True'
								elif obj[8]<=4:
									return 'False'
								else: return 'False'
							elif obj[1]<=1:
								return 'False'
							else: return 'False'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					elif obj[11]>1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[6]>2:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[10]>2.0:
			# {"feature": "Bar", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[9]>1.0:
				# {"feature": "Income", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[8]<=6:
					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[13]<=1:
						return 'False'
					elif obj[13]>1:
						return 'True'
					else: return 'True'
				elif obj[8]>6:
					return 'True'
				else: return 'True'
			elif obj[9]<=1.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]>3:
		# {"feature": "Occupation", "instances": 15, "metric_value": 0.9183, "depth": 2}
		if obj[7]>6:
			# {"feature": "Age", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[1]>1:
					# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[8]<=3:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]>0:
							# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[10]>0.0:
								return 'True'
							elif obj[10]<=0.0:
								return 'False'
							else: return 'False'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[8]>3:
						return 'True'
					else: return 'True'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			elif obj[4]>2:
				return 'True'
			else: return 'True'
		elif obj[7]<=6:
			return 'False'
		else: return 'False'
	else: return 'False'

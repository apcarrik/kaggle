def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[4]>0:
		# {"feature": "Passanger", "instances": 29, "metric_value": 0.9923, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Bar", "instances": 23, "metric_value": 0.9986, "depth": 3}
			if obj[6]>0.0:
				# {"feature": "Age", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[3]>1:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[10]<=2:
						# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[8]>1.0:
							return 'True'
						elif obj[8]<=1.0:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]>1:
								# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5]<=3:
									return 'True'
								elif obj[5]>3:
									return 'False'
								else: return 'False'
							elif obj[1]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[10]>2:
						return 'False'
					else: return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[6]<=0.0:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[5]>2:
					# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]>2:
							return 'True'
						elif obj[3]<=2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[5]<=2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]>2:
			# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[5]<=5:
				return 'False'
			elif obj[5]>5:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[4]<=0:
		# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.9024, "depth": 2}
		if obj[7]>0.0:
			# {"feature": "Occupation", "instances": 19, "metric_value": 0.7425, "depth": 3}
			if obj[5]<=12:
				# {"feature": "Age", "instances": 15, "metric_value": 0.3534, "depth": 4}
				if obj[3]<=6:
					return 'True'
				elif obj[3]>6:
					return 'False'
				else: return 'False'
			elif obj[5]>12:
				# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]<=2:
					return 'False'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[7]<=0.0:
			return 'False'
		else: return 'False'
	else: return 'True'

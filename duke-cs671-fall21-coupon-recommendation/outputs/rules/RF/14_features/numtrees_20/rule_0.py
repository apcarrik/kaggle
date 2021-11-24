def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[2]>1:
		# {"feature": "Age", "instances": 31, "metric_value": 0.9072, "depth": 2}
		if obj[4]>0:
			# {"feature": "Income", "instances": 26, "metric_value": 0.7793, "depth": 3}
			if obj[8]<=6:
				# {"feature": "Direction_same", "instances": 21, "metric_value": 0.8631, "depth": 4}
				if obj[12]<=0:
					# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.9183, "depth": 5}
					if obj[10]<=1.0:
						# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 6}
						if obj[11]<=1.0:
							# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[1]>0:
								# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]>2:
										return 'False'
									elif obj[7]<=2:
										return 'True'
									else: return 'True'
								elif obj[3]>0:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[11]>1.0:
							return 'True'
						else: return 'True'
					elif obj[10]>1.0:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[0]<=2:
							return 'True'
						elif obj[0]>2:
							# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]<=0:
								return 'False'
							elif obj[3]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[12]>0:
					return 'True'
				else: return 'True'
			elif obj[8]>6:
				return 'True'
			else: return 'True'
		elif obj[4]<=0:
			# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[6]<=3:
				return 'False'
			elif obj[6]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Time", "instances": 20, "metric_value": 0.8813, "depth": 2}
		if obj[1]>1:
			# {"feature": "Income", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[8]<=6:
				# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[10]>0.0:
					return 'True'
				elif obj[10]<=0.0:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]<=2:
						return 'False'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[8]>6:
				return 'False'
			else: return 'False'
		elif obj[1]<=1:
			return 'False'
		else: return 'False'
	else: return 'False'

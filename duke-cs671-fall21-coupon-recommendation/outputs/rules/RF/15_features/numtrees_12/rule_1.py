def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Age", "instances": 85, "metric_value": 0.9774, "depth": 1}
	if obj[5]<=5:
		# {"feature": "Coupon", "instances": 73, "metric_value": 0.9966, "depth": 2}
		if obj[2]>1:
			# {"feature": "Occupation", "instances": 47, "metric_value": 0.9441, "depth": 3}
			if obj[8]<=14:
				# {"feature": "Direction_same", "instances": 45, "metric_value": 0.9183, "depth": 4}
				if obj[13]<=0:
					# {"feature": "Passanger", "instances": 41, "metric_value": 0.9474, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.9923, "depth": 6}
						if obj[12]>0.0:
							# {"feature": "Time", "instances": 23, "metric_value": 0.9321, "depth": 7}
							if obj[1]>1:
								# {"feature": "Gender", "instances": 12, "metric_value": 0.65, "depth": 8}
								if obj[4]>0:
									return 'True'
								elif obj[4]<=0:
									# {"feature": "Income", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[9]>1:
										return 'False'
									elif obj[9]<=1:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[1]<=1:
								# {"feature": "Bar", "instances": 11, "metric_value": 0.994, "depth": 8}
								if obj[10]<=1.0:
									# {"feature": "Coupon_validity", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[3]<=0:
										# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[4]<=0:
											# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[6]<=0:
												return 'True'
											elif obj[6]>0:
												return 'False'
											else: return 'False'
										elif obj[4]>0:
											return 'False'
										else: return 'False'
									elif obj[3]>0:
										return 'True'
									else: return 'True'
								elif obj[10]>1.0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[12]<=0.0:
							# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[14]>1:
								return 'False'
							elif obj[14]<=1:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]>0:
									return 'True'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[0]>2:
						# {"feature": "Coupon_validity", "instances": 12, "metric_value": 0.65, "depth": 6}
						if obj[3]<=0:
							return 'True'
						elif obj[3]>0:
							# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[14]<=1:
								return 'True'
							elif obj[14]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[13]>0:
					return 'True'
				else: return 'True'
			elif obj[8]>14:
				return 'False'
			else: return 'False'
		elif obj[2]<=1:
			# {"feature": "Bar", "instances": 26, "metric_value": 0.9306, "depth": 3}
			if obj[10]>0.0:
				# {"feature": "Income", "instances": 19, "metric_value": 0.998, "depth": 4}
				if obj[9]>3:
					# {"feature": "Distance", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[14]>1:
						return 'False'
					elif obj[14]<=1:
						# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[7]>0:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]>0:
								# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[8]>6:
									return 'True'
								elif obj[8]<=6:
									return 'False'
								else: return 'False'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						elif obj[7]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[9]<=3:
					# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[12]>1.0:
						# {"feature": "Coffeehouse", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[11]>0.0:
							return 'False'
						elif obj[11]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[12]<=1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[10]<=0.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[5]>5:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.4138, "depth": 2}
		if obj[8]<=11:
			return 'True'
		elif obj[8]>11:
			return 'False'
		else: return 'False'
	else: return 'True'

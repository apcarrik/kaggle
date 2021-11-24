def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9991, "depth": 1}
	if obj[10]<=11:
		# {"feature": "Education", "instances": 69, "metric_value": 0.9742, "depth": 2}
		if obj[9]>0:
			# {"feature": "Weather", "instances": 46, "metric_value": 0.9986, "depth": 3}
			if obj[1]<=0:
				# {"feature": "Restaurantlessthan20", "instances": 36, "metric_value": 0.9911, "depth": 4}
				if obj[14]<=3.0:
					# {"feature": "Coupon", "instances": 33, "metric_value": 0.9673, "depth": 5}
					if obj[3]>3:
						# {"feature": "Income", "instances": 19, "metric_value": 0.998, "depth": 6}
						if obj[11]<=6:
							# {"feature": "Maritalstatus", "instances": 17, "metric_value": 0.9774, "depth": 7}
							if obj[7]<=1:
								# {"feature": "Age", "instances": 13, "metric_value": 0.8905, "depth": 8}
								if obj[6]>1:
									# {"feature": "Time", "instances": 9, "metric_value": 0.9911, "depth": 9}
									if obj[2]>0:
										# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 10}
										if obj[0]>1:
											# {"feature": "Coupon_validity", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[4]<=0:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8]>0:
														return 'True'
													elif obj[8]<=0:
														return 'False'
													else: return 'False'
												elif obj[5]>0:
													return 'True'
												else: return 'True'
											elif obj[4]>0:
												return 'False'
											else: return 'False'
										elif obj[0]<=1:
											return 'False'
										else: return 'False'
									elif obj[2]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]<=1:
									return 'False'
								else: return 'False'
							elif obj[7]>1:
								# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[17]<=2:
									return 'True'
								elif obj[17]>2:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[11]>6:
							return 'True'
						else: return 'True'
					elif obj[3]<=3:
						# {"feature": "Bar", "instances": 14, "metric_value": 0.7496, "depth": 6}
						if obj[12]>0.0:
							# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[17]>1:
								# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[0]>1:
									# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6]<=1:
										return 'True'
									elif obj[6]>1:
										return 'False'
									else: return 'False'
								elif obj[0]<=1:
									return 'False'
								else: return 'False'
							elif obj[17]<=1:
								return 'True'
							else: return 'True'
						elif obj[12]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[14]>3.0:
					return 'False'
				else: return 'False'
			elif obj[1]>0:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[15]<=1.0:
					return 'False'
				elif obj[15]>1.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[9]<=0:
			# {"feature": "Distance", "instances": 23, "metric_value": 0.6666, "depth": 3}
			if obj[17]>1:
				return 'True'
			elif obj[17]<=1:
				# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[13]>0.0:
					# {"feature": "Coupon_validity", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[4]<=0:
						return 'True'
					elif obj[4]>0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[13]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[10]>11:
		# {"feature": "Coupon_validity", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[4]>0:
			return 'False'
		elif obj[4]<=0:
			# {"feature": "Restaurantlessthan20", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[14]>2.0:
				return 'False'
			elif obj[14]<=2.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'

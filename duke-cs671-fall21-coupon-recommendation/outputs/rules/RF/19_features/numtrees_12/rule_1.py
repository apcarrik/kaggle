def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9991, "depth": 1}
	if obj[0]>0:
		# {"feature": "Coupon_validity", "instances": 79, "metric_value": 0.999, "depth": 2}
		if obj[5]<=0:
			# {"feature": "Coupon", "instances": 43, "metric_value": 0.9523, "depth": 3}
			if obj[4]>1:
				# {"feature": "Education", "instances": 32, "metric_value": 0.8113, "depth": 4}
				if obj[10]>0:
					# {"feature": "Age", "instances": 20, "metric_value": 0.971, "depth": 5}
					if obj[7]<=4:
						# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.8113, "depth": 6}
						if obj[14]>1.0:
							# {"feature": "Maritalstatus", "instances": 11, "metric_value": 0.4395, "depth": 7}
							if obj[8]<=1:
								return 'True'
							elif obj[8]>1:
								return 'False'
							else: return 'False'
						elif obj[14]<=1.0:
							# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[9]<=0:
								return 'False'
							elif obj[9]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[7]>4:
						return 'False'
					else: return 'False'
				elif obj[10]<=0:
					return 'True'
				else: return 'True'
			elif obj[4]<=1:
				# {"feature": "Time", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[3]<=3:
					return 'False'
				elif obj[3]>3:
					# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[7]>0:
						return 'True'
					elif obj[7]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[5]>0:
			# {"feature": "Restaurant20to50", "instances": 36, "metric_value": 0.888, "depth": 3}
			if obj[16]<=1.0:
				# {"feature": "Age", "instances": 27, "metric_value": 0.9751, "depth": 4}
				if obj[7]<=4:
					# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.8865, "depth": 5}
					if obj[14]>0.0:
						# {"feature": "Education", "instances": 19, "metric_value": 0.9495, "depth": 6}
						if obj[10]<=2:
							# {"feature": "Income", "instances": 16, "metric_value": 0.9887, "depth": 7}
							if obj[12]>1:
								# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 8}
								if obj[11]<=17:
									# {"feature": "Restaurantlessthan20", "instances": 11, "metric_value": 0.994, "depth": 9}
									if obj[15]>1.0:
										# {"feature": "Weather", "instances": 9, "metric_value": 0.9911, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Children", "instances": 8, "metric_value": 0.9544, "depth": 11}
											if obj[9]>0:
												# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[2]>55:
													# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[4]>3:
														return 'True'
													elif obj[4]<=3:
														return 'False'
													else: return 'False'
												elif obj[2]<=55:
													return 'False'
												else: return 'False'
											elif obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[1]>1:
											return 'False'
										else: return 'False'
									elif obj[15]<=1.0:
										return 'False'
									else: return 'False'
								elif obj[11]>17:
									return 'True'
								else: return 'True'
							elif obj[12]<=1:
								return 'False'
							else: return 'False'
						elif obj[10]>2:
							return 'False'
						else: return 'False'
					elif obj[14]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[7]>4:
					return 'True'
				else: return 'True'
			elif obj[16]>1.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]<=0:
		return 'True'
	else: return 'True'

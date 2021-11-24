def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Age", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[6]<=5:
		# {"feature": "Maritalstatus", "instances": 72, "metric_value": 1.0, "depth": 2}
		if obj[7]<=1:
			# {"feature": "Passanger", "instances": 57, "metric_value": 0.9819, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Education", "instances": 35, "metric_value": 0.9994, "depth": 4}
				if obj[9]<=3:
					# {"feature": "Coupon", "instances": 31, "metric_value": 0.9812, "depth": 5}
					if obj[3]>0:
						# {"feature": "Coupon_validity", "instances": 26, "metric_value": 1.0, "depth": 6}
						if obj[4]>0:
							# {"feature": "Occupation", "instances": 19, "metric_value": 0.9495, "depth": 7}
							if obj[10]>1:
								# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.8366, "depth": 8}
								if obj[15]>0.0:
									# {"feature": "Bar", "instances": 14, "metric_value": 0.7496, "depth": 9}
									if obj[12]>0.0:
										# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.8454, "depth": 10}
										if obj[13]<=2.0:
											# {"feature": "Income", "instances": 9, "metric_value": 0.9183, "depth": 11}
											if obj[11]<=4:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.8113, "depth": 12}
												if obj[5]<=0:
													return 'False'
												elif obj[5]>0:
													# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[1]<=0:
														# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8]>0:
															return 'False'
														elif obj[8]<=0:
															return 'True'
														else: return 'True'
													elif obj[1]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]>4:
												return 'True'
											else: return 'True'
										elif obj[13]>2.0:
											return 'False'
										else: return 'False'
									elif obj[12]<=0.0:
										return 'False'
									else: return 'False'
								elif obj[15]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[10]<=1:
								# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[12]<=1.0:
									return 'True'
								elif obj[12]>1.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[4]<=0:
							# {"feature": "Weather", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[1]<=0:
								return 'True'
							elif obj[1]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				elif obj[9]>3:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Education", "instances": 22, "metric_value": 0.8454, "depth": 4}
				if obj[9]<=3:
					# {"feature": "Restaurantlessthan20", "instances": 20, "metric_value": 0.7219, "depth": 5}
					if obj[14]<=2.0:
						# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.9183, "depth": 6}
						if obj[13]>0.0:
							# {"feature": "Occupation", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[10]<=6:
								# {"feature": "Weather", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[1]<=0:
									# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[12]<=1.0:
										return 'False'
									elif obj[12]>1.0:
										return 'True'
									else: return 'True'
								elif obj[1]>0:
									return 'True'
								else: return 'True'
							elif obj[10]>6:
								return 'True'
							else: return 'True'
						elif obj[13]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[14]>2.0:
						return 'True'
					else: return 'True'
				elif obj[9]>3:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[7]>1:
			# {"feature": "Income", "instances": 15, "metric_value": 0.7219, "depth": 3}
			if obj[11]<=4:
				return 'False'
			elif obj[11]>4:
				# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]<=3:
					return 'True'
				elif obj[3]>3:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[6]>5:
		# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[13]>0.0:
			return 'True'
		elif obj[13]<=0.0:
			# {"feature": "Maritalstatus", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[7]<=1:
				return 'False'
			elif obj[7]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'

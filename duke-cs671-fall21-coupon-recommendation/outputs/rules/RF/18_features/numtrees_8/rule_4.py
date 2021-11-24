def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Restaurant20to50", "instances": 127, "metric_value": 0.9838, "depth": 1}
	if obj[15]<=2.0:
		# {"feature": "Distance", "instances": 120, "metric_value": 0.9928, "depth": 2}
		if obj[17]<=2:
			# {"feature": "Maritalstatus", "instances": 108, "metric_value": 0.9799, "depth": 3}
			if obj[7]<=1:
				# {"feature": "Bar", "instances": 91, "metric_value": 0.9957, "depth": 4}
				if obj[12]>0.0:
					# {"feature": "Income", "instances": 57, "metric_value": 0.9495, "depth": 5}
					if obj[11]<=3:
						# {"feature": "Education", "instances": 31, "metric_value": 0.7706, "depth": 6}
						if obj[9]>0:
							# {"feature": "Restaurantlessthan20", "instances": 22, "metric_value": 0.9024, "depth": 7}
							if obj[14]>1.0:
								# {"feature": "Coupon_validity", "instances": 20, "metric_value": 0.8113, "depth": 8}
								if obj[4]>0:
									# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.994, "depth": 9}
									if obj[13]<=2.0:
										# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[3]>2:
												# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[6]<=1:
													return 'True'
												elif obj[6]>1:
													return 'False'
												else: return 'False'
											elif obj[3]<=2:
												return 'False'
											else: return 'False'
										elif obj[0]>1:
											return 'True'
										else: return 'True'
									elif obj[13]>2.0:
										return 'False'
									else: return 'False'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							elif obj[14]<=1.0:
								return 'False'
							else: return 'False'
						elif obj[9]<=0:
							return 'True'
						else: return 'True'
					elif obj[11]>3:
						# {"feature": "Direction_same", "instances": 26, "metric_value": 0.9957, "depth": 6}
						if obj[16]<=0:
							# {"feature": "Passanger", "instances": 20, "metric_value": 0.9341, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Coupon_validity", "instances": 11, "metric_value": 0.684, "depth": 8}
								if obj[4]>0:
									return 'False'
								elif obj[4]<=0:
									# {"feature": "Restaurantlessthan20", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[14]<=1.0:
										return 'False'
									elif obj[14]>1.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[0]>2:
								# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[9]<=3:
									# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 9}
									if obj[6]<=4:
										return 'True'
									elif obj[6]>4:
										# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[10]<=7:
											return 'False'
										elif obj[10]>7:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[9]>3:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[16]>0:
							# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[13]<=3.0:
								return 'True'
							elif obj[13]>3.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[12]<=0.0:
					# {"feature": "Passanger", "instances": 34, "metric_value": 0.9597, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Coupon", "instances": 25, "metric_value": 0.795, "depth": 6}
						if obj[3]>0:
							# {"feature": "Occupation", "instances": 19, "metric_value": 0.8997, "depth": 7}
							if obj[10]<=6:
								# {"feature": "Time", "instances": 15, "metric_value": 0.971, "depth": 8}
								if obj[2]>0:
									# {"feature": "Age", "instances": 9, "metric_value": 0.9911, "depth": 9}
									if obj[6]<=4:
										# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.9544, "depth": 10}
										if obj[14]>1.0:
											# {"feature": "Children", "instances": 6, "metric_value": 1.0, "depth": 11}
											if obj[8]>0:
												# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[9]>1:
													# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[11]>2:
														return 'False'
													elif obj[11]<=2:
														return 'True'
													else: return 'True'
												elif obj[9]<=1:
													return 'True'
												else: return 'True'
											elif obj[8]<=0:
												return 'False'
											else: return 'False'
										elif obj[14]<=1.0:
											return 'True'
										else: return 'True'
									elif obj[6]>4:
										return 'False'
									else: return 'False'
								elif obj[2]<=0:
									# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[6]<=6:
										return 'False'
									elif obj[6]>6:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[10]>6:
								return 'False'
							else: return 'False'
						elif obj[3]<=0:
							return 'False'
						else: return 'False'
					elif obj[0]>2:
						# {"feature": "Coupon", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[3]<=3:
							return 'True'
						elif obj[3]>3:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[7]>1:
				# {"feature": "Age", "instances": 17, "metric_value": 0.6723, "depth": 4}
				if obj[6]>1:
					return 'True'
				elif obj[6]<=1:
					# {"feature": "Income", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[11]<=3:
						# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[9]>1:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=1:
								return 'True'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						elif obj[9]<=1:
							return 'False'
						else: return 'False'
					elif obj[11]>3:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[17]>2:
			# {"feature": "Age", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[6]<=4:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[10]<=19:
					return 'False'
				elif obj[10]>19:
					return 'True'
				else: return 'True'
			elif obj[6]>4:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[15]>2.0:
		return 'True'
	else: return 'True'

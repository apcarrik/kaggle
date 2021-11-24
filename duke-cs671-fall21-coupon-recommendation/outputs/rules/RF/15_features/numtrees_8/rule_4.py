def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Education", "instances": 127, "metric_value": 0.9899, "depth": 1}
	if obj[7]<=2:
		# {"feature": "Occupation", "instances": 98, "metric_value": 0.9563, "depth": 2}
		if obj[8]<=7:
			# {"feature": "Passanger", "instances": 66, "metric_value": 0.866, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Income", "instances": 42, "metric_value": 0.9737, "depth": 4}
				if obj[9]>1:
					# {"feature": "Coffeehouse", "instances": 35, "metric_value": 0.9275, "depth": 5}
					if obj[11]<=3.0:
						# {"feature": "Bar", "instances": 32, "metric_value": 0.9544, "depth": 6}
						if obj[10]<=2.0:
							# {"feature": "Coupon", "instances": 31, "metric_value": 0.9383, "depth": 7}
							if obj[2]<=3:
								# {"feature": "Gender", "instances": 22, "metric_value": 0.8454, "depth": 8}
								if obj[4]<=0:
									# {"feature": "Age", "instances": 12, "metric_value": 0.9799, "depth": 9}
									if obj[5]>0:
										# {"feature": "Time", "instances": 11, "metric_value": 0.9457, "depth": 10}
										if obj[1]>0:
											# {"feature": "Coupon_validity", "instances": 10, "metric_value": 0.971, "depth": 11}
											if obj[3]>0:
												# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[13]>0:
													# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[6]<=0:
														# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]>1.0:
															return 'True'
														elif obj[12]<=1.0:
															return 'False'
														else: return 'False'
													elif obj[6]>0:
														return 'False'
													else: return 'False'
												elif obj[13]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[13]<=0:
													# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[12]>0.0:
														# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[6]<=0:
															# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[14]<=3:
																return 'True'
															else: return 'True'
														else: return 'True'
													elif obj[12]<=0.0:
														return 'False'
													else: return 'False'
												elif obj[13]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]<=0:
										return 'False'
									else: return 'False'
								elif obj[4]>0:
									# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.469, "depth": 9}
									if obj[12]>0.0:
										return 'True'
									elif obj[12]<=0.0:
										# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[6]>0:
											return 'True'
										elif obj[6]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[2]>3:
								# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[12]>-1.0:
									# {"feature": "Coupon_validity", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[3]>0:
										# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 10}
										if obj[4]>0:
											# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[5]<=3:
												# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[1]<=0:
													# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[6]>0:
														# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[14]<=1:
															return 'False'
														elif obj[14]>1:
															return 'True'
														else: return 'True'
													elif obj[6]<=0:
														return 'False'
													else: return 'False'
												elif obj[1]>0:
													return 'False'
												else: return 'False'
											elif obj[5]>3:
												return 'True'
											else: return 'True'
										elif obj[4]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								elif obj[12]<=-1.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[10]>2.0:
							return 'False'
						else: return 'False'
					elif obj[11]>3.0:
						return 'True'
					else: return 'True'
				elif obj[9]<=1:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[2]>2:
						return 'False'
					elif obj[2]<=2:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=1:
							return 'True'
						elif obj[1]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Income", "instances": 24, "metric_value": 0.4138, "depth": 4}
				if obj[9]<=4:
					return 'True'
				elif obj[9]>4:
					# {"feature": "Coupon", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[2]>1:
						# {"feature": "Time", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]>1:
								return 'True'
							elif obj[5]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[8]>7:
			# {"feature": "Income", "instances": 32, "metric_value": 0.9887, "depth": 3}
			if obj[9]>0:
				# {"feature": "Age", "instances": 27, "metric_value": 0.999, "depth": 4}
				if obj[5]>0:
					# {"feature": "Distance", "instances": 20, "metric_value": 0.9341, "depth": 5}
					if obj[14]<=2:
						# {"feature": "Bar", "instances": 17, "metric_value": 0.7871, "depth": 6}
						if obj[10]<=0.0:
							# {"feature": "Passanger", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[2]<=3:
									return 'True'
								elif obj[2]>3:
									# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[1]<=0:
										return 'False'
									elif obj[1]>0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						elif obj[10]>0.0:
							return 'True'
						else: return 'True'
					elif obj[14]>2:
						return 'False'
					else: return 'False'
				elif obj[5]<=0:
					# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[12]<=1.0:
						return 'False'
					elif obj[12]>1.0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]>0:
							return 'True'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[9]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[7]>2:
		# {"feature": "Occupation", "instances": 29, "metric_value": 0.9294, "depth": 2}
		if obj[8]<=12:
			# {"feature": "Coupon", "instances": 24, "metric_value": 0.8113, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Gender", "instances": 16, "metric_value": 0.5436, "depth": 4}
				if obj[4]<=0:
					# {"feature": "Age", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[5]<=4:
						# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[3]>0:
								return 'False'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						elif obj[1]>3:
							return 'True'
						else: return 'True'
					elif obj[5]>4:
						return 'False'
					else: return 'False'
				elif obj[4]>0:
					return 'False'
				else: return 'False'
			elif obj[2]>3:
				# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[0]>1:
					# {"feature": "Income", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[9]>4:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=3:
							return 'False'
						elif obj[5]>3:
							return 'True'
						else: return 'True'
					elif obj[9]<=4:
						return 'True'
					else: return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[8]>12:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[2]>0:
				return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'

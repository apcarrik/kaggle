def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Age", "instances": 127, "metric_value": 0.9946, "depth": 1}
	if obj[5]<=3:
		# {"feature": "Occupation", "instances": 66, "metric_value": 0.9894, "depth": 2}
		if obj[8]<=20:
			# {"feature": "Income", "instances": 60, "metric_value": 0.9992, "depth": 3}
			if obj[9]>0:
				# {"feature": "Time", "instances": 54, "metric_value": 0.9841, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Coffeehouse", "instances": 29, "metric_value": 0.8498, "depth": 5}
					if obj[11]>0.0:
						# {"feature": "Direction_same", "instances": 22, "metric_value": 0.5746, "depth": 6}
						if obj[13]<=0:
							return 'False'
						elif obj[13]>0:
							# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[2]<=3:
								# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0]<=1:
									return 'False'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							elif obj[2]>3:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[11]<=0.0:
						# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[7]>0:
							return 'True'
						elif obj[7]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]>1:
					# {"feature": "Coupon", "instances": 25, "metric_value": 0.971, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Education", "instances": 17, "metric_value": 0.874, "depth": 6}
						if obj[7]>1:
							# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.9799, "depth": 7}
							if obj[11]<=3.0:
								# {"feature": "Bar", "instances": 10, "metric_value": 1.0, "depth": 8}
								if obj[10]<=1.0:
									# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[14]<=2:
										# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 10}
										if obj[12]>0.0:
											# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 11}
											if obj[0]>1:
												# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[6]<=0:
													return 'True'
												elif obj[6]>0:
													# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[3]<=0:
														return 'True'
													elif obj[3]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[0]<=1:
												# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[4]>0:
													return 'True'
												elif obj[4]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[12]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[14]>2:
										return 'False'
									else: return 'False'
								elif obj[10]>1.0:
									return 'False'
								else: return 'False'
							elif obj[11]>3.0:
								return 'True'
							else: return 'True'
						elif obj[7]<=1:
							return 'True'
						else: return 'True'
					elif obj[2]>3:
						# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[11]<=1.0:
							# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[4]<=0:
								# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]>0:
									return 'False'
								elif obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[4]>0:
								return 'True'
							else: return 'True'
						elif obj[11]>1.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[9]<=0:
				return 'True'
			else: return 'True'
		elif obj[8]>20:
			return 'False'
		else: return 'False'
	elif obj[5]>3:
		# {"feature": "Time", "instances": 61, "metric_value": 0.9288, "depth": 2}
		if obj[1]>0:
			# {"feature": "Restaurant20to50", "instances": 45, "metric_value": 0.9911, "depth": 3}
			if obj[12]<=2.0:
				# {"feature": "Bar", "instances": 41, "metric_value": 0.9996, "depth": 4}
				if obj[10]>0.0:
					# {"feature": "Income", "instances": 22, "metric_value": 0.9457, "depth": 5}
					if obj[9]<=7:
						# {"feature": "Gender", "instances": 17, "metric_value": 0.9975, "depth": 6}
						if obj[4]<=0:
							# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 7}
							if obj[2]<=3:
								# {"feature": "Passanger", "instances": 10, "metric_value": 0.7219, "depth": 8}
								if obj[0]<=2:
									# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[14]>1:
										# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											return 'True'
										else: return 'True'
									elif obj[14]<=1:
										return 'True'
									else: return 'True'
								elif obj[0]>2:
									return 'True'
								else: return 'True'
							elif obj[2]>3:
								# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]>0:
							return 'False'
						else: return 'False'
					elif obj[9]>7:
						return 'True'
					else: return 'True'
				elif obj[10]<=0.0:
					# {"feature": "Coupon", "instances": 19, "metric_value": 0.9495, "depth": 5}
					if obj[2]>1:
						# {"feature": "Gender", "instances": 14, "metric_value": 1.0, "depth": 6}
						if obj[4]>0:
							# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[8]<=5:
								return 'True'
							elif obj[8]>5:
								return 'False'
							else: return 'False'
						elif obj[4]<=0:
							# {"feature": "Income", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[9]>1:
								return 'False'
							elif obj[9]<=1:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[13]>0:
									return 'True'
								elif obj[13]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[12]>2.0:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.3373, "depth": 3}
			if obj[12]>0.0:
				return 'True'
			elif obj[12]<=0.0:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	else: return 'True'

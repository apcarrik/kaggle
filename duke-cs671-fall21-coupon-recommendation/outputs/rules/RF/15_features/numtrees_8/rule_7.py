def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coffeehouse", "instances": 127, "metric_value": 0.9899, "depth": 1}
	if obj[11]<=3.0:
		# {"feature": "Passanger", "instances": 119, "metric_value": 0.9774, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Distance", "instances": 78, "metric_value": 0.9995, "depth": 3}
			if obj[14]>1:
				# {"feature": "Occupation", "instances": 43, "metric_value": 0.9523, "depth": 4}
				if obj[8]>1:
					# {"feature": "Direction_same", "instances": 40, "metric_value": 0.9097, "depth": 5}
					if obj[13]<=0:
						# {"feature": "Coupon", "instances": 35, "metric_value": 0.9518, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Income", "instances": 19, "metric_value": 0.998, "depth": 7}
							if obj[9]<=6:
								# {"feature": "Gender", "instances": 17, "metric_value": 0.9774, "depth": 8}
								if obj[4]<=0:
									# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.971, "depth": 9}
									if obj[12]>0.0:
										# {"feature": "Children", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[6]<=0:
											# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[3]>0:
												return 'False'
											elif obj[3]<=0:
												# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[10]>2.0:
													return 'True'
												elif obj[10]<=2.0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[6]>0:
											return 'True'
										else: return 'True'
									elif obj[12]<=0.0:
										return 'False'
									else: return 'False'
								elif obj[4]>0:
									# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 9}
									if obj[5]<=4:
										return 'True'
									elif obj[5]>4:
										# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[9]>6:
								return 'False'
							else: return 'False'
						elif obj[2]>3:
							# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.6962, "depth": 7}
							if obj[12]>-1.0:
								# {"feature": "Education", "instances": 15, "metric_value": 0.5665, "depth": 8}
								if obj[7]>0:
									return 'False'
								elif obj[7]<=0:
									# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[5]<=4:
										# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[9]<=4:
											return 'True'
										elif obj[9]>4:
											return 'False'
										else: return 'False'
									elif obj[5]>4:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[12]<=-1.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[13]>0:
						return 'False'
					else: return 'False'
				elif obj[8]<=1:
					return 'True'
				else: return 'True'
			elif obj[14]<=1:
				# {"feature": "Time", "instances": 35, "metric_value": 0.8981, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Occupation", "instances": 18, "metric_value": 0.5033, "depth": 5}
					if obj[8]>6:
						return 'True'
					elif obj[8]<=6:
						# {"feature": "Coupon_validity", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[3]<=0:
							# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[4]>0:
									return 'True'
								elif obj[4]<=0:
									return 'False'
								else: return 'False'
							elif obj[2]>2:
								return 'False'
							else: return 'False'
						elif obj[3]>0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[1]>1:
					# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.9975, "depth": 5}
					if obj[12]<=2.0:
						# {"feature": "Coupon", "instances": 14, "metric_value": 0.9403, "depth": 6}
						if obj[2]>1:
							# {"feature": "Income", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[9]>3:
								return 'True'
							elif obj[9]<=3:
								return 'False'
							else: return 'False'
						elif obj[2]<=1:
							return 'False'
						else: return 'False'
					elif obj[12]>2.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Occupation", "instances": 41, "metric_value": 0.839, "depth": 3}
			if obj[8]>6:
				# {"feature": "Gender", "instances": 22, "metric_value": 0.5746, "depth": 4}
				if obj[4]>0:
					# {"feature": "Coupon", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[2]>1:
						# {"feature": "Children", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[6]>0:
							# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[5]<=6:
									return 'True'
								elif obj[5]>6:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[14]>1:
										return 'True'
									elif obj[14]<=1:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[1]>2:
								return 'False'
							else: return 'False'
						elif obj[6]<=0:
							return 'True'
						else: return 'True'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			elif obj[8]<=6:
				# {"feature": "Bar", "instances": 19, "metric_value": 0.9819, "depth": 4}
				if obj[10]<=1.0:
					# {"feature": "Coupon", "instances": 15, "metric_value": 0.9968, "depth": 5}
					if obj[2]>0:
						# {"feature": "Income", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[9]<=4:
							# {"feature": "Age", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[5]>0:
								# {"feature": "Coupon_validity", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[3]>0:
									# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[1]<=0:
										# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6]>0:
											return 'False'
										elif obj[6]<=0:
											return 'True'
										else: return 'True'
									elif obj[1]>0:
										return 'False'
									else: return 'False'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[9]>4:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[10]>1.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[11]>3.0:
		# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[14]<=2:
			return 'False'
		elif obj[14]>2:
			# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]<=2:
				return 'False'
			elif obj[2]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'

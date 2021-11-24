def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9924, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Distance", "instances": 83, "metric_value": 0.9822, "depth": 2}
		if obj[12]>1:
			# {"feature": "Occupation", "instances": 47, "metric_value": 0.9035, "depth": 3}
			if obj[7]>2:
				# {"feature": "Bar", "instances": 38, "metric_value": 0.7897, "depth": 4}
				if obj[8]<=1.0:
					# {"feature": "Gender", "instances": 25, "metric_value": 0.5294, "depth": 5}
					if obj[3]<=0:
						# {"feature": "Age", "instances": 13, "metric_value": 0.7793, "depth": 6}
						if obj[4]<=4:
							# {"feature": "Children", "instances": 9, "metric_value": 0.5033, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[1]<=2:
									return 'False'
								elif obj[1]>2:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]>4:
							# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[1]>0:
								# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2]>2:
									# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[6]<=0:
										return 'False'
									elif obj[6]>0:
										return 'True'
									else: return 'True'
								elif obj[2]<=2:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[3]>0:
						return 'False'
					else: return 'False'
				elif obj[8]>1.0:
					# {"feature": "Age", "instances": 13, "metric_value": 0.9957, "depth": 5}
					if obj[4]>1:
						# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[10]>-1.0:
								# {"feature": "Gender", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[9]<=2.0:
										# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1]<=1:
											# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[6]<=2:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[9]>2.0:
										return 'True'
									else: return 'True'
								elif obj[3]>0:
									return 'True'
								else: return 'True'
							elif obj[10]<=-1.0:
								return 'False'
							else: return 'False'
						elif obj[2]>3:
							return 'False'
						else: return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[7]<=2:
				# {"feature": "Time", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]>1:
							# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3]>0:
								return 'False'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						elif obj[4]<=1:
							return 'True'
						else: return 'True'
					elif obj[2]>3:
						return 'False'
					else: return 'False'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[12]<=1:
			# {"feature": "Coffeehouse", "instances": 36, "metric_value": 0.9911, "depth": 3}
			if obj[9]<=3.0:
				# {"feature": "Occupation", "instances": 31, "metric_value": 0.9992, "depth": 4}
				if obj[7]<=10:
					# {"feature": "Time", "instances": 22, "metric_value": 0.976, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Education", "instances": 19, "metric_value": 0.998, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Coupon", "instances": 16, "metric_value": 0.9887, "depth": 7}
							if obj[2]>1:
								# {"feature": "Gender", "instances": 12, "metric_value": 0.9799, "depth": 8}
								if obj[3]>0:
									# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[5]>0:
											# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[10]<=1.0:
												return 'False'
											elif obj[10]>1.0:
												return 'True'
											else: return 'True'
										elif obj[5]<=0:
											return 'True'
										else: return 'True'
									elif obj[4]>2:
										return 'True'
									else: return 'True'
								elif obj[3]<=0:
									# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[4]>1:
										return 'False'
									elif obj[4]<=1:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[2]<=1:
								return 'False'
							else: return 'False'
						elif obj[6]>2:
							return 'True'
						else: return 'True'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				elif obj[7]>10:
					# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[10]<=3.0:
						# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[2]>2:
							return 'False'
						elif obj[2]<=2:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]>0:
								return 'False'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[10]>3.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[9]>3.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Occupation", "instances": 44, "metric_value": 0.7309, "depth": 2}
		if obj[7]>0:
			# {"feature": "Age", "instances": 43, "metric_value": 0.6931, "depth": 3}
			if obj[4]>1:
				# {"feature": "Time", "instances": 27, "metric_value": 0.8256, "depth": 4}
				if obj[1]>0:
					# {"feature": "Distance", "instances": 22, "metric_value": 0.9024, "depth": 5}
					if obj[12]>1:
						# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[9]<=3.0:
							# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[10]<=1.0:
								# {"feature": "Bar", "instances": 8, "metric_value": 1.0, "depth": 8}
								if obj[8]>0.0:
									# {"feature": "Children", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[5]>0:
										# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[2]>0:
											# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[6]>0:
												return 'True'
											elif obj[6]<=0:
												return 'False'
											else: return 'False'
										elif obj[2]<=0:
											return 'False'
										else: return 'False'
									elif obj[5]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[10]>1.0:
								return 'True'
							else: return 'True'
						elif obj[9]>3.0:
							return 'False'
						else: return 'False'
					elif obj[12]<=1:
						# {"feature": "Gender", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[3]>0:
							return 'True'
						elif obj[3]<=0:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]<=3:
								return 'True'
							elif obj[2]>3:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[4]<=1:
				# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.3373, "depth": 4}
				if obj[9]>0.0:
					return 'True'
				elif obj[9]<=0.0:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>2:
						return 'False'
					elif obj[1]<=2:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[7]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'

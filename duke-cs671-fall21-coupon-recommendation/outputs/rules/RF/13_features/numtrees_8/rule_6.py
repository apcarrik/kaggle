def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Occupation", "instances": 127, "metric_value": 0.9838, "depth": 1}
	if obj[7]<=14.668146703969164:
		# {"feature": "Time", "instances": 104, "metric_value": 0.9471, "depth": 2}
		if obj[1]>1:
			# {"feature": "Coffeehouse", "instances": 62, "metric_value": 0.8238, "depth": 3}
			if obj[9]>1.0:
				# {"feature": "Restaurant20to50", "instances": 32, "metric_value": 0.6253, "depth": 4}
				if obj[10]<=1.0:
					# {"feature": "Children", "instances": 20, "metric_value": 0.2864, "depth": 5}
					if obj[5]<=0:
						return 'True'
					elif obj[5]>0:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[2]<=2:
							return 'True'
						elif obj[2]>2:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>2:
								return 'True'
							elif obj[0]<=2:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[10]>1.0:
					# {"feature": "Coupon", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[4]>0:
							# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[8]>0.0:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[3]>0:
										# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5]>0:
											return 'True'
										elif obj[5]<=0:
											return 'False'
										else: return 'False'
									elif obj[3]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[0]>2:
								return 'True'
							else: return 'True'
						elif obj[4]<=0:
							return 'False'
						else: return 'False'
					elif obj[2]>2:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[9]<=1.0:
				# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.9481, "depth": 4}
				if obj[10]<=1.0:
					# {"feature": "Direction_same", "instances": 19, "metric_value": 0.998, "depth": 5}
					if obj[11]<=0:
						# {"feature": "Passanger", "instances": 17, "metric_value": 0.9774, "depth": 6}
						if obj[0]>0:
							# {"feature": "Education", "instances": 16, "metric_value": 0.9544, "depth": 7}
							if obj[6]<=3:
								# {"feature": "Age", "instances": 12, "metric_value": 1.0, "depth": 8}
								if obj[4]>1:
									# {"feature": "Bar", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[2]<=2:
											# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[12]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'False'
											else: return 'False'
										elif obj[2]>2:
											# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[12]>1:
												# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[3]<=1:
													# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[5]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[12]<=1:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]>1.0:
										return 'False'
									else: return 'False'
								elif obj[4]<=1:
									# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[2]>0:
										return 'True'
									elif obj[2]<=0:
										# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5]<=0:
											return 'True'
										elif obj[5]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[6]>3:
								return 'True'
							else: return 'True'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[11]>0:
						return 'False'
					else: return 'False'
				elif obj[10]>1.0:
					# {"feature": "Bar", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[8]<=2.0:
						# {"feature": "Age", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[4]>0:
							return 'True'
						elif obj[4]<=0:
							# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[0]>1:
								# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2]>2:
									return 'True'
								elif obj[2]<=2:
									return 'False'
								else: return 'False'
							elif obj[0]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[8]>2.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Passanger", "instances": 42, "metric_value": 0.9984, "depth": 3}
			if obj[0]>0:
				# {"feature": "Coupon", "instances": 39, "metric_value": 0.9881, "depth": 4}
				if obj[2]>0:
					# {"feature": "Education", "instances": 32, "metric_value": 1.0, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.9544, "depth": 6}
						if obj[10]>0.0:
							# {"feature": "Distance", "instances": 20, "metric_value": 0.8113, "depth": 7}
							if obj[12]>1:
								# {"feature": "Bar", "instances": 12, "metric_value": 0.9799, "depth": 8}
								if obj[8]<=0.0:
									# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[3]>0:
										# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[4]>1:
											# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[5]<=0:
												# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[9]<=0.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[11]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[5]>0:
												return 'False'
											else: return 'False'
										elif obj[4]<=1:
											return 'True'
										else: return 'True'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								elif obj[8]>0.0:
									return 'True'
								else: return 'True'
							elif obj[12]<=1:
								return 'True'
							else: return 'True'
						elif obj[10]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[6]>2:
						# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[9]>0.0:
							return 'False'
						elif obj[9]<=0.0:
							# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]>0:
								return 'False'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[2]<=0:
					# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[6]<=3:
						return 'False'
					elif obj[6]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[7]>14.668146703969164:
		# {"feature": "Coupon", "instances": 23, "metric_value": 0.8865, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Time", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[1]>0:
				# {"feature": "Age", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[4]<=4:
					# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[8]<=1.0:
						return 'False'
					elif obj[8]>1.0:
						# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]>0:
								return 'True'
							elif obj[6]<=0:
								return 'False'
							else: return 'False'
						elif obj[0]>2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[4]>4:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[2]>3:
			# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[9]>-1.0:
				return 'False'
			elif obj[9]<=-1.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'

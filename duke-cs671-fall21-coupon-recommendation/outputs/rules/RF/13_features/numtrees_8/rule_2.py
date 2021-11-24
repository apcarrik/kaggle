def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Occupation", "instances": 127, "metric_value": 0.9621, "depth": 1}
	if obj[7]<=7.551181102362205:
		# {"feature": "Education", "instances": 87, "metric_value": 0.8799, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Restaurant20to50", "instances": 69, "metric_value": 0.7554, "depth": 3}
			if obj[10]>0.0:
				# {"feature": "Coffeehouse", "instances": 61, "metric_value": 0.8047, "depth": 4}
				if obj[9]>1.0:
					# {"feature": "Coupon", "instances": 32, "metric_value": 0.6253, "depth": 5}
					if obj[2]>1:
						# {"feature": "Time", "instances": 23, "metric_value": 0.4262, "depth": 6}
						if obj[1]<=3:
							return 'True'
						elif obj[1]>3:
							# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[0]>1:
								# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[4]>1:
									# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[5]<=0:
										return 'True'
									elif obj[5]>0:
										return 'False'
									else: return 'False'
								elif obj[4]<=1:
									return 'True'
								else: return 'True'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[2]<=1:
						# {"feature": "Children", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[8]<=1.0:
								# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[4]<=5:
									return 'False'
								elif obj[4]>5:
									return 'True'
								else: return 'True'
							elif obj[8]>1.0:
								return 'True'
							else: return 'True'
						elif obj[5]>0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[9]<=1.0:
					# {"feature": "Coupon", "instances": 29, "metric_value": 0.9294, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Children", "instances": 20, "metric_value": 0.8113, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Age", "instances": 15, "metric_value": 0.5665, "depth": 7}
							if obj[4]>0:
								# {"feature": "Direction_same", "instances": 14, "metric_value": 0.3712, "depth": 8}
								if obj[11]<=0:
									return 'True'
								elif obj[11]>0:
									return 'False'
								else: return 'False'
							elif obj[4]<=0:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[1]>0:
								# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[8]<=1.0:
									return 'False'
								elif obj[8]>1.0:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[2]>3:
						# {"feature": "Children", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[11]<=0:
								return 'False'
							elif obj[11]>0:
								return 'True'
							else: return 'True'
						elif obj[5]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[10]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[6]>2:
			# {"feature": "Age", "instances": 18, "metric_value": 0.9641, "depth": 3}
			if obj[4]>1:
				# {"feature": "Direction_same", "instances": 14, "metric_value": 1.0, "depth": 4}
				if obj[11]<=0:
					# {"feature": "Coupon", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[2]>1:
						# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[9]<=3.0:
							# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[0]>1:
									# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]<=0.0:
										return 'False'
									elif obj[8]>0.0:
										return 'True'
									else: return 'True'
								elif obj[0]<=1:
									return 'True'
								else: return 'True'
							elif obj[3]>0:
								return 'True'
							else: return 'True'
						elif obj[9]>3.0:
							return 'False'
						else: return 'False'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				elif obj[11]>0:
					return 'True'
				else: return 'True'
			elif obj[4]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[7]>7.551181102362205:
		# {"feature": "Coupon", "instances": 40, "metric_value": 0.9837, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Distance", "instances": 28, "metric_value": 0.9963, "depth": 3}
			if obj[12]<=2:
				# {"feature": "Education", "instances": 24, "metric_value": 0.9544, "depth": 4}
				if obj[6]>0:
					# {"feature": "Bar", "instances": 21, "metric_value": 0.9852, "depth": 5}
					if obj[8]<=3.0:
						# {"feature": "Age", "instances": 20, "metric_value": 0.971, "depth": 6}
						if obj[4]>0:
							# {"feature": "Time", "instances": 17, "metric_value": 0.9975, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Gender", "instances": 15, "metric_value": 0.971, "depth": 8}
								if obj[3]>0:
									# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 9}
									if obj[9]<=1.0:
										# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[0]>0:
											# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[5]>0:
												# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[10]<=0.0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[11]<=0:
														return 'False'
													else: return 'False'
												elif obj[10]>0.0:
													return 'True'
												else: return 'True'
											elif obj[5]<=0:
												return 'True'
											else: return 'True'
										elif obj[0]<=0:
											return 'False'
										else: return 'False'
									elif obj[9]>1.0:
										return 'False'
									else: return 'False'
								elif obj[3]<=0:
									# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[9]>-1.0:
										return 'True'
									elif obj[9]<=-1.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[1]>3:
								return 'False'
							else: return 'False'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					elif obj[8]>3.0:
						return 'False'
					else: return 'False'
				elif obj[6]<=0:
					return 'True'
				else: return 'True'
			elif obj[12]>2:
				return 'False'
			else: return 'False'
		elif obj[2]>3:
			# {"feature": "Time", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[1]<=3:
				return 'False'
			elif obj[1]>3:
				# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]>0:
					return 'True'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	else: return 'False'

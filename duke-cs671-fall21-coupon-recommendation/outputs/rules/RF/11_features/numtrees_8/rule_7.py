def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coffeehouse", "instances": 127, "metric_value": 1.0, "depth": 1}
	if obj[7]>1.0:
		# {"feature": "Restaurant20to50", "instances": 65, "metric_value": 0.9501, "depth": 2}
		if obj[8]<=2.0:
			# {"feature": "Age", "instances": 59, "metric_value": 0.9066, "depth": 3}
			if obj[3]<=6:
				# {"feature": "Occupation", "instances": 55, "metric_value": 0.9299, "depth": 4}
				if obj[5]<=19:
					# {"feature": "Direction_same", "instances": 52, "metric_value": 0.9471, "depth": 5}
					if obj[9]<=0:
						# {"feature": "Coupon", "instances": 43, "metric_value": 0.8841, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Distance", "instances": 31, "metric_value": 0.7706, "depth": 7}
							if obj[10]>1:
								# {"feature": "Time", "instances": 26, "metric_value": 0.8404, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Education", "instances": 16, "metric_value": 0.6962, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Bar", "instances": 10, "metric_value": 0.8813, "depth": 10}
										if obj[6]<=1.0:
											return 'True'
										elif obj[6]>1.0:
											# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[0]<=1:
												return 'False'
											elif obj[0]>1:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[4]>2:
										return 'True'
									else: return 'True'
								elif obj[1]>2:
									# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 10}
										if obj[0]>2:
											# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[6]>0.0:
												return 'True'
											elif obj[6]<=0.0:
												return 'False'
											else: return 'False'
										elif obj[0]<=2:
											return 'True'
										else: return 'True'
									elif obj[4]>2:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[10]<=1:
								return 'True'
							else: return 'True'
						elif obj[2]>3:
							# {"feature": "Distance", "instances": 12, "metric_value": 1.0, "depth": 7}
							if obj[10]>1:
								# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[1]<=3:
									return 'False'
								elif obj[1]>3:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0]>1:
										# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[4]<=0:
											return 'False'
										elif obj[4]>0:
											return 'True'
										else: return 'True'
									elif obj[0]<=1:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[10]<=1:
								# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[4]<=2:
									return 'True'
								elif obj[4]>2:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[9]>0:
						# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=1.0:
							# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[4]>0:
								# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0]<=1:
									return 'False'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]>1.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[5]>19:
					return 'True'
				else: return 'True'
			elif obj[3]>6:
				return 'True'
			else: return 'True'
		elif obj[8]>2.0:
			# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[1]<=3:
				return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[7]<=1.0:
		# {"feature": "Coupon", "instances": 62, "metric_value": 0.9514, "depth": 2}
		if obj[2]>1:
			# {"feature": "Age", "instances": 43, "metric_value": 0.9996, "depth": 3}
			if obj[3]>1:
				# {"feature": "Distance", "instances": 33, "metric_value": 0.9673, "depth": 4}
				if obj[10]<=2:
					# {"feature": "Education", "instances": 30, "metric_value": 0.9871, "depth": 5}
					if obj[4]<=3:
						# {"feature": "Occupation", "instances": 29, "metric_value": 0.9784, "depth": 6}
						if obj[5]>6:
							# {"feature": "Bar", "instances": 17, "metric_value": 0.9975, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "Passanger", "instances": 12, "metric_value": 0.9799, "depth": 8}
								if obj[0]<=2:
									# {"feature": "Time", "instances": 10, "metric_value": 0.8813, "depth": 9}
									if obj[1]>2:
										# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[8]<=0.0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[8]>0.0:
											return 'False'
										else: return 'False'
									elif obj[1]<=2:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[8]<=0.0:
												return 'True'
											elif obj[8]>0.0:
												return 'False'
											else: return 'False'
										elif obj[9]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[0]>2:
									return 'True'
								else: return 'True'
							elif obj[6]>0.0:
								# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[0]<=1:
									return 'True'
								elif obj[0]>1:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[5]<=6:
							# {"feature": "Bar", "instances": 12, "metric_value": 0.8113, "depth": 7}
							if obj[6]<=0.0:
								# {"feature": "Direction_same", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[9]<=0:
									# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[8]<=1.0:
										# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[1]<=0:
												return 'False'
											elif obj[1]>0:
												return 'False'
											else: return 'False'
										elif obj[0]>1:
											return 'True'
										else: return 'True'
									elif obj[8]>1.0:
										return 'False'
									else: return 'False'
								elif obj[9]>0:
									return 'False'
								else: return 'False'
							elif obj[6]>0.0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]>3:
						return 'True'
					else: return 'True'
				elif obj[10]>2:
					return 'False'
				else: return 'False'
			elif obj[3]<=1:
				# {"feature": "Bar", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[6]<=1.0:
					# {"feature": "Time", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[1]<=3:
						return 'True'
					elif obj[1]>3:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]>13:
							return 'True'
						elif obj[5]<=13:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]>1.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]<=1:
			# {"feature": "Age", "instances": 19, "metric_value": 0.4855, "depth": 3}
			if obj[3]<=2:
				return 'False'
			elif obj[3]>2:
				# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[6]>0.0:
						return 'True'
					elif obj[6]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'

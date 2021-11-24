def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9946, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Education", "instances": 87, "metric_value": 0.9396, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Distance", "instances": 65, "metric_value": 0.8717, "depth": 3}
			if obj[9]<=2:
				# {"feature": "Time", "instances": 57, "metric_value": 0.8043, "depth": 4}
				if obj[1]>1:
					# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.9481, "depth": 5}
					if obj[7]>0.0:
						# {"feature": "Bar", "instances": 27, "metric_value": 0.9751, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.9852, "depth": 7}
							if obj[6]<=2.0:
								# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 8}
								if obj[4]<=5:
									# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[0]>1:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[0]<=1:
										return 'False'
									else: return 'False'
								elif obj[4]>5:
									# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[0]>2:
										return 'True'
									elif obj[0]<=2:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[6]>2.0:
								return 'False'
							else: return 'False'
						elif obj[5]>0.0:
							# {"feature": "Occupation", "instances": 13, "metric_value": 0.7793, "depth": 7}
							if obj[4]>5:
								# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=2.0:
									# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[0]>1:
										# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[0]<=1:
										return 'False'
									else: return 'False'
								elif obj[6]>2.0:
									return 'True'
								else: return 'True'
							elif obj[4]<=5:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[7]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[1]<=1:
					# {"feature": "Bar", "instances": 27, "metric_value": 0.5033, "depth": 5}
					if obj[5]<=0.0:
						# {"feature": "Occupation", "instances": 16, "metric_value": 0.6962, "depth": 6}
						if obj[4]>2:
							# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.8454, "depth": 7}
							if obj[6]>1.0:
								# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[7]>1.0:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[0]<=1:
											return 'False'
										else: return 'False'
									elif obj[8]>0:
										return 'True'
									else: return 'True'
								elif obj[7]<=1.0:
									return 'True'
								else: return 'True'
							elif obj[6]<=1.0:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[8]>0:
									# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[7]<=1.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[8]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]<=2:
							return 'True'
						else: return 'True'
					elif obj[5]>0.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[9]>2:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[4]<=7:
					# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[1]>0:
						# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=1.0:
								return 'False'
							elif obj[6]>1.0:
								return 'True'
							else: return 'True'
						elif obj[5]>0.0:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[4]>7:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[3]>2:
			# {"feature": "Occupation", "instances": 22, "metric_value": 0.994, "depth": 3}
			if obj[4]<=12:
				# {"feature": "Time", "instances": 19, "metric_value": 0.998, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.8905, "depth": 5}
					if obj[7]<=2.0:
						# {"feature": "Passanger", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[0]>0:
							# {"feature": "Coffeehouse", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[6]<=2.0:
								# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[5]<=0.0:
									return 'False'
								elif obj[5]>0.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]>0:
										return 'True'
									elif obj[8]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[6]>2.0:
								# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[5]>1.0:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[9]<=1:
										return 'False'
									elif obj[9]>1:
										return 'True'
									else: return 'True'
								elif obj[5]<=1.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[7]>2.0:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[6]>0.0:
							return 'False'
						elif obj[6]<=0.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[4]>12:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]>3:
		# {"feature": "Coffeehouse", "instances": 40, "metric_value": 0.9097, "depth": 2}
		if obj[6]<=2.0:
			# {"feature": "Occupation", "instances": 31, "metric_value": 0.7706, "depth": 3}
			if obj[4]<=8:
				# {"feature": "Passanger", "instances": 16, "metric_value": 0.9544, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[7]<=1.0:
						return 'False'
					elif obj[7]>1.0:
						# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[8]<=0:
							return 'True'
						elif obj[8]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[3]<=2:
						return 'True'
					elif obj[3]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]>8:
				# {"feature": "Education", "instances": 15, "metric_value": 0.3534, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=0:
						return 'False'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[6]>2.0:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[4]>6:
				# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[3]>0:
					# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[8]<=0:
						return 'False'
					elif obj[8]>0:
						return 'True'
					else: return 'True'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			elif obj[4]<=6:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'

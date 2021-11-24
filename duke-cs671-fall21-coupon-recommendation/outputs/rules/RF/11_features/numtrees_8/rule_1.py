def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Education", "instances": 127, "metric_value": 0.9838, "depth": 1}
	if obj[4]<=2:
		# {"feature": "Coupon", "instances": 94, "metric_value": 0.9252, "depth": 2}
		if obj[2]>1:
			# {"feature": "Bar", "instances": 67, "metric_value": 0.793, "depth": 3}
			if obj[6]<=2.0:
				# {"feature": "Age", "instances": 58, "metric_value": 0.7007, "depth": 4}
				if obj[3]<=4:
					# {"feature": "Restaurant20to50", "instances": 47, "metric_value": 0.785, "depth": 5}
					if obj[8]>-1.0:
						# {"feature": "Occupation", "instances": 46, "metric_value": 0.7554, "depth": 6}
						if obj[5]<=10:
							# {"feature": "Coffeehouse", "instances": 33, "metric_value": 0.6136, "depth": 7}
							if obj[7]<=3.0:
								# {"feature": "Distance", "instances": 31, "metric_value": 0.5548, "depth": 8}
								if obj[10]>1:
									# {"feature": "Direction_same", "instances": 17, "metric_value": 0.3228, "depth": 9}
									if obj[9]<=0:
										return 'True'
									elif obj[9]>0:
										# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1]<=0:
											return 'True'
										elif obj[1]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[10]<=1:
									# {"feature": "Direction_same", "instances": 14, "metric_value": 0.7496, "depth": 9}
									if obj[9]<=0:
										# {"feature": "Time", "instances": 10, "metric_value": 0.8813, "depth": 10}
										if obj[1]>0:
											# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 11}
											if obj[0]>2:
												return 'True'
											elif obj[0]<=2:
												return 'True'
											else: return 'True'
										elif obj[1]<=0:
											# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[0]<=1:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[9]>0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]>3.0:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]<=2:
									return 'True'
								elif obj[1]>2:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[5]>10:
							# {"feature": "Direction_same", "instances": 13, "metric_value": 0.9612, "depth": 7}
							if obj[9]<=0:
								# {"feature": "Coffeehouse", "instances": 10, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0.0:
									# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[1]<=2:
										# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=1:
												return 'True'
											else: return 'True'
										elif obj[0]>1:
											# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=2:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[1]>2:
										return 'False'
									else: return 'False'
								elif obj[7]>0.0:
									# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[0]>1:
										return 'True'
									elif obj[0]<=1:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[9]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[8]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[3]>4:
					return 'True'
				else: return 'True'
			elif obj[6]>2.0:
				# {"feature": "Age", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[3]>1:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[0]<=2:
						return 'False'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=1:
			# {"feature": "Passanger", "instances": 27, "metric_value": 0.9751, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Age", "instances": 23, "metric_value": 0.8865, "depth": 4}
				if obj[3]>0:
					# {"feature": "Occupation", "instances": 19, "metric_value": 0.9495, "depth": 5}
					if obj[5]>0:
						# {"feature": "Bar", "instances": 18, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=2.0:
							# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.874, "depth": 7}
							if obj[8]<=2.0:
								# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.8113, "depth": 8}
								if obj[7]>0.0:
									# {"feature": "Distance", "instances": 13, "metric_value": 0.6194, "depth": 9}
									if obj[10]<=1:
										# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 10}
										if obj[1]>0:
											# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[1]<=0:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[9]<=1:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[10]>1:
										return 'False'
									else: return 'False'
								elif obj[7]<=0.0:
									# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[1]>0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=3:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[8]>2.0:
								return 'True'
							else: return 'True'
						elif obj[6]>2.0:
							return 'True'
						else: return 'True'
					elif obj[5]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[4]>2:
		# {"feature": "Coffeehouse", "instances": 33, "metric_value": 0.9183, "depth": 2}
		if obj[7]<=3.0:
			# {"feature": "Occupation", "instances": 24, "metric_value": 0.9799, "depth": 3}
			if obj[5]<=14:
				# {"feature": "Time", "instances": 22, "metric_value": 0.994, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Age", "instances": 17, "metric_value": 0.9367, "depth": 5}
					if obj[3]>1:
						# {"feature": "Direction_same", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[9]<=0:
							return 'False'
						elif obj[9]>0:
							# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[2]>1:
								# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[8]>0.0:
									# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6]<=1.0:
											# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=1:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[8]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[2]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[3]<=1:
						# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[2]>1:
							# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[8]>2.0:
									return 'True'
								elif obj[8]<=2.0:
									return 'False'
								else: return 'False'
							elif obj[6]>1.0:
								return 'False'
							else: return 'False'
						elif obj[2]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[1]>3:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]>14:
				return 'False'
			else: return 'False'
		elif obj[7]>3.0:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[5]>1:
				return 'False'
			elif obj[5]<=1:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=0:
					return 'False'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	else: return 'False'

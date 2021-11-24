def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Bar", "instances": 127, "metric_value": 0.9566, "depth": 1}
	if obj[5]<=2.0:
		# {"feature": "Coupon", "instances": 109, "metric_value": 0.9824, "depth": 2}
		if obj[2]>0:
			# {"feature": "Distance", "instances": 94, "metric_value": 0.9441, "depth": 3}
			if obj[9]<=2:
				# {"feature": "Coffeehouse", "instances": 77, "metric_value": 0.8951, "depth": 4}
				if obj[6]<=1.0:
					# {"feature": "Education", "instances": 41, "metric_value": 0.9789, "depth": 5}
					if obj[3]<=3:
						# {"feature": "Occupation", "instances": 39, "metric_value": 0.9881, "depth": 6}
						if obj[4]<=20:
							# {"feature": "Restaurant20to50", "instances": 37, "metric_value": 0.9953, "depth": 7}
							if obj[7]<=3.0:
								# {"feature": "Time", "instances": 36, "metric_value": 0.9978, "depth": 8}
								if obj[1]>1:
									# {"feature": "Direction_same", "instances": 27, "metric_value": 0.999, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Passanger", "instances": 26, "metric_value": 1.0, "depth": 10}
										if obj[0]>1:
											return 'False'
										elif obj[0]<=1:
											return 'True'
										else: return 'True'
									elif obj[8]>0:
										return 'False'
									else: return 'False'
								elif obj[1]<=1:
									# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 9}
									if obj[0]>0:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.8113, "depth": 10}
										if obj[8]<=0:
											return 'True'
										elif obj[8]>0:
											return 'True'
										else: return 'True'
									elif obj[0]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[7]>3.0:
								return 'True'
							else: return 'True'
						elif obj[4]>20:
							return 'True'
						else: return 'True'
					elif obj[3]>3:
						return 'True'
					else: return 'True'
				elif obj[6]>1.0:
					# {"feature": "Education", "instances": 36, "metric_value": 0.7107, "depth": 5}
					if obj[3]>0:
						# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.8404, "depth": 6}
						if obj[7]<=2.0:
							# {"feature": "Occupation", "instances": 24, "metric_value": 0.7383, "depth": 7}
							if obj[4]<=9:
								# {"feature": "Direction_same", "instances": 17, "metric_value": 0.874, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Time", "instances": 14, "metric_value": 0.9403, "depth": 9}
									if obj[1]>1:
										# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 10}
										if obj[0]>2:
											return 'True'
										elif obj[0]<=2:
											return 'True'
										else: return 'True'
									elif obj[1]<=1:
										# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[0]<=1:
											return 'False'
										elif obj[0]>1:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[8]>0:
									return 'True'
								else: return 'True'
							elif obj[4]>9:
								return 'True'
							else: return 'True'
						elif obj[7]>2.0:
							return 'False'
						else: return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[9]>2:
				# {"feature": "Occupation", "instances": 17, "metric_value": 0.9774, "depth": 4}
				if obj[4]<=5:
					# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[6]<=0.0:
						# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[3]>0:
							return 'True'
						elif obj[3]<=0:
							# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[7]<=1.0:
								# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]>1.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]>0.0:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]>0:
							return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[4]>5:
					# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[6]<=2.0:
						return 'False'
					elif obj[6]>2.0:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]<=1:
							return 'True'
						elif obj[1]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[2]<=0:
			# {"feature": "Occupation", "instances": 15, "metric_value": 0.7219, "depth": 3}
			if obj[4]>3:
				# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[3]<=3:
						# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[8]<=0:
							return 'False'
						elif obj[8]>0:
							return 'True'
						else: return 'True'
					elif obj[3]>3:
						return 'True'
					else: return 'True'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			elif obj[4]<=3:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[5]>2.0:
		# {"feature": "Distance", "instances": 18, "metric_value": 0.5033, "depth": 2}
		if obj[9]<=2:
			return 'True'
		elif obj[9]>2:
			# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[3]>0:
				return 'True'
			elif obj[3]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'

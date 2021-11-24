def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coffeehouse", "instances": 85, "metric_value": 0.9831, "depth": 1}
	if obj[6]>1.0:
		# {"feature": "Distance", "instances": 44, "metric_value": 0.8757, "depth": 2}
		if obj[9]>1:
			# {"feature": "Passanger", "instances": 25, "metric_value": 0.9896, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Occupation", "instances": 17, "metric_value": 0.9774, "depth": 4}
				if obj[4]>4:
					# {"feature": "Coupon", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[2]>1:
						return 'False'
					elif obj[2]<=1:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=0:
							# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]>1:
								return 'True'
							elif obj[3]<=1:
								return 'False'
							else: return 'False'
						elif obj[1]>0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]<=4:
					# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[2]>0:
							# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[8]<=0:
								return 'True'
							elif obj[8]>0:
								# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]>2:
									return 'True'
								elif obj[3]<=2:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[1]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]>4:
						return 'False'
					elif obj[4]<=4:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[9]<=1:
			# {"feature": "Occupation", "instances": 19, "metric_value": 0.4855, "depth": 3}
			if obj[4]>4:
				return 'True'
			elif obj[4]<=4:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[2]>0:
					# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[3]>1:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[7]<=1.0:
								return 'False'
							elif obj[7]>1.0:
								return 'True'
							else: return 'True'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					elif obj[3]<=1:
						return 'True'
					else: return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[6]<=1.0:
		# {"feature": "Time", "instances": 41, "metric_value": 0.9892, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Occupation", "instances": 21, "metric_value": 0.9852, "depth": 3}
			if obj[4]<=13:
				# {"feature": "Education", "instances": 19, "metric_value": 0.998, "depth": 4}
				if obj[3]<=2:
					# {"feature": "Coupon", "instances": 17, "metric_value": 0.9774, "depth": 5}
					if obj[2]>0:
						# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.9544, "depth": 6}
						if obj[7]>0.0:
							# {"feature": "Bar", "instances": 13, "metric_value": 0.9957, "depth": 7}
							if obj[5]<=3.0:
								# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9799, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Distance", "instances": 11, "metric_value": 0.994, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Passanger", "instances": 10, "metric_value": 1.0, "depth": 10}
										if obj[0]<=1:
											return 'True'
										elif obj[0]>1:
											return 'True'
										else: return 'True'
									elif obj[9]>2:
										return 'True'
									else: return 'True'
								elif obj[8]>0:
									return 'True'
								else: return 'True'
							elif obj[5]>3.0:
								return 'False'
							else: return 'False'
						elif obj[7]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[4]>13:
				return 'True'
			else: return 'True'
		elif obj[1]>2:
			# {"feature": "Occupation", "instances": 20, "metric_value": 0.8813, "depth": 3}
			if obj[4]<=7:
				# {"feature": "Coupon", "instances": 14, "metric_value": 0.9852, "depth": 4}
				if obj[2]<=1:
					# {"feature": "Bar", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[5]<=1.0:
						return 'False'
					elif obj[5]>1.0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]>1:
							return 'False'
						elif obj[0]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]>1:
					# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[3]>0:
						return 'True'
					elif obj[3]<=0:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[4]>7:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Education", "instances": 127, "metric_value": 0.9621, "depth": 1}
	if obj[3]>1:
		# {"feature": "Occupation", "instances": 74, "metric_value": 0.9995, "depth": 2}
		if obj[4]<=8:
			# {"feature": "Time", "instances": 47, "metric_value": 0.9734, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Coupon", "instances": 33, "metric_value": 0.9993, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Bar", "instances": 17, "metric_value": 0.874, "depth": 5}
					if obj[5]<=3.0:
						# {"feature": "Passanger", "instances": 16, "metric_value": 0.8113, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[6]<=3.0:
								# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[7]<=2.0:
									# {"feature": "Distance", "instances": 8, "metric_value": 1.0, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[8]>0:
											return 'True'
										elif obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[9]>2:
										return 'False'
									else: return 'False'
								elif obj[7]>2.0:
									return 'True'
								else: return 'True'
							elif obj[6]>3.0:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[5]>3.0:
						return 'False'
					else: return 'False'
				elif obj[2]>2:
					# {"feature": "Bar", "instances": 16, "metric_value": 0.8113, "depth": 5}
					if obj[5]>-1.0:
						# {"feature": "Distance", "instances": 15, "metric_value": 0.7219, "depth": 6}
						if obj[9]<=2:
							# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.5917, "depth": 7}
							if obj[7]<=2.0:
								# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.4138, "depth": 8}
								if obj[6]<=2.0:
									return 'False'
								elif obj[6]>2.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]>0:
										return 'False'
									elif obj[8]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[7]>2.0:
								# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=1.0:
									return 'True'
								elif obj[6]>1.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[9]>2:
							return 'True'
						else: return 'True'
					elif obj[5]<=-1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]>1:
				# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.5917, "depth": 4}
				if obj[6]<=3.0:
					return 'True'
				elif obj[6]>3.0:
					# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=3:
							return 'False'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]>8:
			# {"feature": "Distance", "instances": 27, "metric_value": 0.8767, "depth": 3}
			if obj[9]<=1:
				# {"feature": "Bar", "instances": 18, "metric_value": 0.9911, "depth": 4}
				if obj[5]<=2.0:
					# {"feature": "Time", "instances": 16, "metric_value": 0.9544, "depth": 5}
					if obj[1]>1:
						# {"feature": "Passanger", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[0]<=2:
							return 'False'
						elif obj[0]>2:
							# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[2]>2:
								# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]>0.0:
									return 'True'
								elif obj[6]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[2]<=2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[1]<=1:
						# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=1.0:
							return 'True'
						elif obj[6]>1.0:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]>1:
								return 'False'
							elif obj[2]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[5]>2.0:
					return 'True'
				else: return 'True'
			elif obj[9]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[3]<=1:
		# {"feature": "Occupation", "instances": 53, "metric_value": 0.7368, "depth": 2}
		if obj[4]>2:
			# {"feature": "Coffeehouse", "instances": 40, "metric_value": 0.8485, "depth": 3}
			if obj[6]>0.0:
				# {"feature": "Coupon", "instances": 34, "metric_value": 0.7335, "depth": 4}
				if obj[2]>1:
					# {"feature": "Time", "instances": 23, "metric_value": 0.4262, "depth": 5}
					if obj[1]>1:
						return 'True'
					elif obj[1]<=1:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[5]>0.0:
								return 'True'
							elif obj[5]<=0.0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[2]<=1:
					# {"feature": "Passanger", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Bar", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[5]<=2.0:
							# {"feature": "Distance", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[9]<=2:
								# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[8]>0:
										# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[7]>1.0:
											return 'True'
										elif obj[7]<=1.0:
											return 'False'
										else: return 'False'
									elif obj[8]<=0:
										return 'True'
									else: return 'True'
								elif obj[1]>1:
									# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[9]>2:
								return 'True'
							else: return 'True'
						elif obj[5]>2.0:
							return 'False'
						else: return 'False'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[6]<=0.0:
				# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[2]>3:
					return 'False'
				elif obj[2]<=3:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]>0:
						# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=0.0:
							return 'False'
						elif obj[5]>0.0:
							return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]<=2:
			return 'True'
		else: return 'True'
	else: return 'True'

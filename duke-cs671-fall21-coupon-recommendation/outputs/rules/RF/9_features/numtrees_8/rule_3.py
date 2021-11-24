def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9507, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Bar", "instances": 75, "metric_value": 0.9999, "depth": 2}
		if obj[5]<=1.0:
			# {"feature": "Direction_same", "instances": 48, "metric_value": 0.9544, "depth": 3}
			if obj[7]<=0:
				# {"feature": "Coupon", "instances": 29, "metric_value": 0.7355, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Occupation", "instances": 17, "metric_value": 0.3228, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=1.0:
							return 'False'
						elif obj[6]>1.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]>2:
					# {"feature": "Education", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[3]>0:
						# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[4]<=7:
								# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[8]>2:
									# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6]<=1.0:
										return 'False'
									else: return 'False'
								elif obj[8]<=2:
									return 'False'
								else: return 'False'
							elif obj[4]>7:
								return 'True'
							else: return 'True'
						elif obj[1]>1:
							return 'False'
						else: return 'False'
					elif obj[3]<=0:
						# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]>1:
							return 'True'
						elif obj[1]<=1:
							# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=1:
								return 'True'
							elif obj[4]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]>0:
				# {"feature": "Time", "instances": 19, "metric_value": 0.9495, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Occupation", "instances": 17, "metric_value": 0.874, "depth": 5}
					if obj[4]<=10:
						# {"feature": "Coupon", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[3]<=2:
								# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[6]>0.0:
									# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[8]<=1:
										return 'True'
									elif obj[8]>1:
										return 'False'
									else: return 'False'
								elif obj[6]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[3]>2:
								return 'False'
							else: return 'False'
						elif obj[2]>2:
							# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]>0.0:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]<=1:
										return 'True'
									else: return 'True'
								elif obj[6]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[3]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]>10:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[5]>1.0:
			# {"feature": "Time", "instances": 27, "metric_value": 0.8256, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Coupon", "instances": 22, "metric_value": 0.9024, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.7425, "depth": 5}
					if obj[6]>-1.0:
						# {"feature": "Distance", "instances": 18, "metric_value": 0.65, "depth": 6}
						if obj[8]<=1:
							# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[4]<=14:
								# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 8}
								if obj[3]<=3:
									# {"feature": "Direction_same", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[7]>0:
										return 'True'
									elif obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[3]>3:
									return 'True'
								else: return 'True'
							elif obj[4]>14:
								return 'False'
							else: return 'False'
						elif obj[8]>1:
							return 'True'
						else: return 'True'
					elif obj[6]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[2]>3:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Coupon", "instances": 52, "metric_value": 0.7063, "depth": 2}
		if obj[2]>0:
			# {"feature": "Bar", "instances": 44, "metric_value": 0.5108, "depth": 3}
			if obj[5]<=2.0:
				# {"feature": "Distance", "instances": 40, "metric_value": 0.3843, "depth": 4}
				if obj[8]>1:
					# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.5033, "depth": 5}
					if obj[6]>0.0:
						# {"feature": "Occupation", "instances": 19, "metric_value": 0.6292, "depth": 6}
						if obj[4]<=6:
							# {"feature": "Time", "instances": 11, "metric_value": 0.4395, "depth": 7}
							if obj[1]>3:
								return 'True'
							elif obj[1]<=3:
								# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]>6:
							# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[1]>0:
								# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[3]>0:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[3]<=0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[8]<=1:
					return 'True'
				else: return 'True'
			elif obj[5]>2.0:
				# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=0:
						# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=17:
							return 'False'
						elif obj[4]>17:
							return 'True'
						else: return 'True'
					elif obj[3]>0:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]<=0:
			# {"feature": "Bar", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[5]<=1.0:
				return 'False'
			elif obj[5]>1.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'

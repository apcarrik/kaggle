def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Bar", "instances": 127, "metric_value": 0.9989, "depth": 1}
	if obj[5]<=1.0:
		# {"feature": "Coupon", "instances": 81, "metric_value": 0.9599, "depth": 2}
		if obj[2]>0:
			# {"feature": "Passanger", "instances": 68, "metric_value": 0.9944, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Direction_same", "instances": 50, "metric_value": 0.958, "depth": 4}
				if obj[7]<=0:
					# {"feature": "Time", "instances": 34, "metric_value": 0.8338, "depth": 5}
					if obj[1]>0:
						# {"feature": "Education", "instances": 21, "metric_value": 0.9183, "depth": 6}
						if obj[3]>0:
							# {"feature": "Distance", "instances": 17, "metric_value": 0.7871, "depth": 7}
							if obj[8]<=2:
								# {"feature": "Occupation", "instances": 13, "metric_value": 0.6194, "depth": 8}
								if obj[4]<=14:
									# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.684, "depth": 9}
									if obj[6]<=1.0:
										return 'False'
									elif obj[6]>1.0:
										return 'False'
									else: return 'False'
								elif obj[4]>14:
									return 'False'
								else: return 'False'
							elif obj[8]>2:
								# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[4]>1:
									# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6]>0.0:
										return 'False'
									elif obj[6]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[4]<=1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[3]<=0:
							# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[4]>2:
								return 'True'
							elif obj[4]<=2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[1]<=0:
						# {"feature": "Occupation", "instances": 13, "metric_value": 0.6194, "depth": 6}
						if obj[4]<=21:
							# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.4138, "depth": 7}
							if obj[6]<=1.0:
								return 'False'
							elif obj[6]>1.0:
								# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[8]<=1:
									return 'False'
								elif obj[8]>1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]>21:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[7]>0:
					# {"feature": "Distance", "instances": 16, "metric_value": 0.9544, "depth": 5}
					if obj[8]<=1:
						# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[6]<=1.0:
							# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 7}
							if obj[4]<=4:
								return 'True'
							elif obj[4]>4:
								# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[1]>0:
									# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]<=0:
										return 'True'
									elif obj[3]>0:
										return 'False'
									else: return 'False'
								elif obj[1]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[6]>1.0:
							return 'False'
						else: return 'False'
					elif obj[8]>1:
						# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=5:
							return 'False'
						elif obj[4]>5:
							# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3]>0:
								return 'True'
							elif obj[3]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Occupation", "instances": 18, "metric_value": 0.9183, "depth": 4}
				if obj[4]>1:
					# {"feature": "Time", "instances": 16, "metric_value": 0.8113, "depth": 5}
					if obj[1]>2:
						# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[8]<=1:
							# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[3]<=2:
								return 'True'
							elif obj[3]>2:
								# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]>0.0:
									return 'True'
								elif obj[6]<=0.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[8]>1:
							# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[6]>0.0:
								return 'False'
							elif obj[6]<=0.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[1]<=2:
						return 'True'
					else: return 'True'
				elif obj[4]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[5]>1.0:
		# {"feature": "Education", "instances": 46, "metric_value": 0.9321, "depth": 2}
		if obj[3]>1:
			# {"feature": "Occupation", "instances": 32, "metric_value": 0.9887, "depth": 3}
			if obj[4]>2:
				# {"feature": "Time", "instances": 23, "metric_value": 0.9877, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Passanger", "instances": 14, "metric_value": 0.8631, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Coupon", "instances": 12, "metric_value": 0.65, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[8]<=1:
								# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[6]>1.0:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[6]<=1.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]>0:
										return 'True'
									elif obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[8]>1:
								return 'False'
							else: return 'False'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[6]>-1.0:
							return 'True'
						elif obj[6]<=-1.0:
							return 'False'
						else: return 'False'
					elif obj[0]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]<=2:
				# {"feature": "Time", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[3]<=1:
			# {"feature": "Distance", "instances": 14, "metric_value": 0.5917, "depth": 3}
			if obj[8]>1:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[4]>1:
					# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[2]>1:
						return 'True'
					elif obj[2]<=1:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]>1:
							return 'True'
						elif obj[0]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]<=1:
					return 'False'
				else: return 'False'
			elif obj[8]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'

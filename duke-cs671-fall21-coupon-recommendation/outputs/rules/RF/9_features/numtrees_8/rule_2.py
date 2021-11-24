def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9899, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Education", "instances": 83, "metric_value": 0.9974, "depth": 2}
		if obj[3]>0:
			# {"feature": "Occupation", "instances": 55, "metric_value": 0.9457, "depth": 3}
			if obj[4]>1:
				# {"feature": "Distance", "instances": 47, "metric_value": 0.8787, "depth": 4}
				if obj[8]<=2:
					# {"feature": "Coupon", "instances": 37, "metric_value": 0.9353, "depth": 5}
					if obj[2]>0:
						# {"feature": "Bar", "instances": 33, "metric_value": 0.9673, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.998, "depth": 7}
							if obj[6]<=2.0:
								# {"feature": "Time", "instances": 18, "metric_value": 1.0, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Direction_same", "instances": 15, "metric_value": 0.9968, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[1]>3:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[6]>2.0:
								return 'False'
							else: return 'False'
						elif obj[5]>1.0:
							# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.8631, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Time", "instances": 11, "metric_value": 0.9457, "depth": 8}
								if obj[1]>1:
									# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[1]<=1:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]>1.0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[8]>2:
					# {"feature": "Bar", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[5]<=2.0:
						return 'False'
					elif obj[5]>2.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]<=1:
				# {"feature": "Bar", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[5]>0.0:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[2]<=1:
						return 'True'
					elif obj[2]>1:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[8]>2:
								return 'True'
							elif obj[8]<=2:
								return 'False'
							else: return 'False'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[5]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]<=0:
			# {"feature": "Coupon", "instances": 28, "metric_value": 0.9059, "depth": 3}
			if obj[2]>0:
				# {"feature": "Occupation", "instances": 24, "metric_value": 0.7383, "depth": 4}
				if obj[4]<=7:
					# {"feature": "Bar", "instances": 17, "metric_value": 0.3228, "depth": 5}
					if obj[5]>0.0:
						return 'True'
					elif obj[5]<=0.0:
						# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]>0:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[8]>1:
								# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=1.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[8]<=1:
								return 'True'
							else: return 'True'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>7:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[8]<=1:
						# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[7]>0:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]<=0:
								# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5]<=0.0:
									return 'False'
								elif obj[5]>0.0:
									return 'True'
								else: return 'True'
							elif obj[1]>0:
								return 'False'
							else: return 'False'
						elif obj[7]<=0:
							return 'True'
						else: return 'True'
					elif obj[8]>1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Occupation", "instances": 44, "metric_value": 0.8454, "depth": 2}
		if obj[4]<=18:
			# {"feature": "Restaurant20to50", "instances": 40, "metric_value": 0.7692, "depth": 3}
			if obj[6]>0.0:
				# {"feature": "Distance", "instances": 34, "metric_value": 0.8338, "depth": 4}
				if obj[8]>1:
					# {"feature": "Bar", "instances": 23, "metric_value": 0.9321, "depth": 5}
					if obj[5]>0.0:
						# {"feature": "Coupon", "instances": 15, "metric_value": 0.9968, "depth": 6}
						if obj[2]>0:
							# {"feature": "Time", "instances": 12, "metric_value": 0.9799, "depth": 7}
							if obj[1]>0:
								# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 8}
								if obj[3]>0:
									# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9911, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[3]<=0:
									return 'False'
								else: return 'False'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[5]<=0.0:
						# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 6}
						if obj[3]<=2:
							return 'True'
						elif obj[3]>2:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=4:
								# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[2]<=3:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[8]<=1:
					# {"feature": "Time", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[5]<=0.0:
							# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[2]>2:
								# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]<=0:
									return 'True'
								elif obj[3]>0:
									return 'False'
								else: return 'False'
							elif obj[2]<=2:
								return 'True'
							else: return 'True'
						elif obj[5]>0.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[6]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[4]>18:
			# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[2]>2:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]>0:
					return 'False'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			elif obj[2]<=2:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'

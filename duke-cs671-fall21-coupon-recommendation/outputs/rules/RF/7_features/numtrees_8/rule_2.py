def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9671, "depth": 1}
	if obj[1]>1:
		# {"feature": "Occupation", "instances": 85, "metric_value": 0.9018, "depth": 2}
		if obj[3]<=10:
			# {"feature": "Education", "instances": 61, "metric_value": 0.8047, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Restaurant20to50", "instances": 50, "metric_value": 0.7219, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Direction_same", "instances": 30, "metric_value": 0.5665, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Distance", "instances": 24, "metric_value": 0.65, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Passanger", "instances": 21, "metric_value": 0.7025, "depth": 7}
							if obj[0]<=1:
								return 'True'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						elif obj[6]>2:
							return 'True'
						else: return 'True'
					elif obj[5]>0:
						return 'True'
					else: return 'True'
				elif obj[4]>1.0:
					# {"feature": "Passanger", "instances": 20, "metric_value": 0.8813, "depth": 5}
					if obj[0]>0:
						# {"feature": "Distance", "instances": 19, "metric_value": 0.8315, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Direction_same", "instances": 17, "metric_value": 0.7871, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[6]>2:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]>2:
				# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[4]<=2.0:
					# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[6]<=1:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					elif obj[6]>1:
						return 'False'
					else: return 'False'
				elif obj[4]>2.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>10:
			# {"feature": "Education", "instances": 24, "metric_value": 1.0, "depth": 3}
			if obj[2]>0:
				# {"feature": "Direction_same", "instances": 18, "metric_value": 0.9641, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.896, "depth": 5}
					if obj[4]>1.0:
						# {"feature": "Passanger", "instances": 11, "metric_value": 0.684, "depth": 6}
						if obj[0]>1:
							# {"feature": "Distance", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						elif obj[0]<=1:
							# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[6]<=1:
								return 'False'
							elif obj[6]>1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]<=1.0:
						# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[0]>0:
								return 'True'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[5]>0:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[6]<=1:
							return 'False'
						elif obj[6]>1:
							return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Occupation", "instances": 42, "metric_value": 0.9934, "depth": 2}
		if obj[3]<=14:
			# {"feature": "Restaurant20to50", "instances": 39, "metric_value": 0.9995, "depth": 3}
			if obj[4]<=3.0:
				# {"feature": "Education", "instances": 37, "metric_value": 0.9953, "depth": 4}
				if obj[2]<=4:
					# {"feature": "Passanger", "instances": 36, "metric_value": 0.9911, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Direction_same", "instances": 24, "metric_value": 0.9544, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 17, "metric_value": 0.9774, "depth": 7}
							if obj[6]<=2:
								return 'False'
							elif obj[6]>2:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[6]<=1:
								return 'False'
							elif obj[6]>1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[0]>1:
						# {"feature": "Distance", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[2]>4:
					return 'True'
				else: return 'True'
			elif obj[4]>3.0:
				return 'True'
			else: return 'True'
		elif obj[3]>14:
			return 'False'
		else: return 'False'
	else: return 'False'

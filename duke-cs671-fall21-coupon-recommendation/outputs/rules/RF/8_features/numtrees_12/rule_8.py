def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9831, "depth": 1}
	if obj[1]>1:
		# {"feature": "Occupation", "instances": 62, "metric_value": 0.889, "depth": 2}
		if obj[3]>4:
			# {"feature": "Distance", "instances": 40, "metric_value": 0.971, "depth": 3}
			if obj[7]<=2:
				# {"feature": "Education", "instances": 36, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Bar", "instances": 33, "metric_value": 0.9457, "depth": 5}
					if obj[4]>0.0:
						# {"feature": "Passanger", "instances": 17, "metric_value": 0.9975, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[5]>1.0:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]>1:
							# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[5]>1.0:
								return 'True'
							elif obj[5]<=1.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[4]<=0.0:
						# {"feature": "Passanger", "instances": 16, "metric_value": 0.8113, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 10, "metric_value": 0.469, "depth": 7}
							if obj[6]<=0:
								return 'True'
							elif obj[6]>0:
								# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[5]<=1.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[0]>1:
							# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[5]>0.0:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[5]<=0.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			elif obj[7]>2:
				return 'False'
			else: return 'False'
		elif obj[3]<=4:
			# {"feature": "Distance", "instances": 22, "metric_value": 0.5746, "depth": 3}
			if obj[7]>1:
				# {"feature": "Direction_same", "instances": 14, "metric_value": 0.7496, "depth": 4}
				if obj[6]<=0:
					# {"feature": "Education", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[2]>0:
						# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[5]>0.0:
							# {"feature": "Bar", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[4]<=0.0:
								return 'True'
							elif obj[4]>0.0:
								# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[0]<=1:
									return 'True'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]<=0.0:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]<=3:
								# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]<=0.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				elif obj[6]>0:
					return 'False'
				else: return 'False'
			elif obj[7]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[1]<=1:
		# {"feature": "Occupation", "instances": 23, "metric_value": 0.8281, "depth": 2}
		if obj[3]<=13:
			# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9183, "depth": 3}
			if obj[5]>0.0:
				# {"feature": "Bar", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[4]<=2.0:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[7]>1:
						# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[2]>0:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[2]<=0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					elif obj[7]<=1:
						return 'False'
					else: return 'False'
				elif obj[4]>2.0:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]>1:
						return 'True'
					elif obj[2]<=1:
						# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[6]>0:
							return 'True'
						elif obj[6]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[5]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[3]>13:
			return 'False'
		else: return 'False'
	else: return 'False'

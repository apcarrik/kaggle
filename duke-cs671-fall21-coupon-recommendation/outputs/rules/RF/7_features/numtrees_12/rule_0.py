def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Distance", "instances": 57, "metric_value": 0.9819, "depth": 2}
		if obj[6]<=1:
			# {"feature": "Occupation", "instances": 29, "metric_value": 0.9923, "depth": 3}
			if obj[3]<=14:
				# {"feature": "Education", "instances": 27, "metric_value": 0.9751, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Coupon", "instances": 22, "metric_value": 0.9024, "depth": 5}
					if obj[1]>1:
						# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.9774, "depth": 6}
						if obj[4]<=2.0:
							# {"feature": "Direction_same", "instances": 16, "metric_value": 0.9887, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[4]>2.0:
							return 'True'
						else: return 'True'
					elif obj[1]<=1:
						return 'True'
					else: return 'True'
				elif obj[2]>2:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[1]<=1:
						return 'False'
					elif obj[1]>1:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=1.0:
							return 'False'
						elif obj[4]>1.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[3]>14:
				return 'False'
			else: return 'False'
		elif obj[6]>1:
			# {"feature": "Occupation", "instances": 28, "metric_value": 0.8631, "depth": 3}
			if obj[3]<=21:
				# {"feature": "Coupon", "instances": 26, "metric_value": 0.7793, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Education", "instances": 14, "metric_value": 0.3712, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[4]>0.0:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[4]<=0.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[1]>1:
					# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[2]<=1:
							# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[2]>1:
							return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[2]>1:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[2]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[3]>21:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Coupon", "instances": 28, "metric_value": 0.8113, "depth": 2}
		if obj[1]>1:
			# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.684, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "Occupation", "instances": 18, "metric_value": 0.7642, "depth": 4}
				if obj[3]>2:
					# {"feature": "Education", "instances": 17, "metric_value": 0.6723, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Direction_same", "instances": 15, "metric_value": 0.7219, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 15, "metric_value": 0.7219, "depth": 7}
							if obj[6]>1:
								return 'True'
							elif obj[6]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[2]>3:
						return 'True'
					else: return 'True'
				elif obj[3]<=2:
					return 'False'
				else: return 'False'
			elif obj[4]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[2]>1:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]>12:
					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=2:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]<=12:
					return 'True'
				else: return 'True'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'

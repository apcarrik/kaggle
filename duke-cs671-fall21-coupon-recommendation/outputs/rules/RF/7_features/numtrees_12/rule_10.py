def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Education", "instances": 85, "metric_value": 0.9991, "depth": 1}
	if obj[2]>0:
		# {"feature": "Restaurant20to50", "instances": 57, "metric_value": 0.9621, "depth": 2}
		if obj[4]>0.0:
			# {"feature": "Occupation", "instances": 49, "metric_value": 0.9113, "depth": 3}
			if obj[3]>6:
				# {"feature": "Coupon", "instances": 25, "metric_value": 0.9988, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Distance", "instances": 15, "metric_value": 0.9183, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Passanger", "instances": 12, "metric_value": 0.8113, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[0]>2:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]>2:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[1]>3:
					# {"feature": "Passanger", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[0]>1:
						# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[6]<=1:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[6]>1:
							return 'True'
						else: return 'True'
					elif obj[0]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[3]<=6:
				# {"feature": "Direction_same", "instances": 24, "metric_value": 0.65, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Distance", "instances": 18, "metric_value": 0.7642, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[1]>1:
							# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[0]>0:
								return 'False'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						elif obj[1]<=1:
							# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]>2:
						return 'False'
					else: return 'False'
				elif obj[5]>0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[4]<=0.0:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]<=0:
		# {"feature": "Distance", "instances": 28, "metric_value": 0.7496, "depth": 2}
		if obj[6]>1:
			# {"feature": "Coupon", "instances": 17, "metric_value": 0.9367, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[3]<=12:
					return 'True'
				elif obj[3]>12:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]>3:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[3]>3:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[4]>1.0:
						# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[3]<=3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]<=1:
			return 'True'
		else: return 'True'
	else: return 'True'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[4]<=2.0:
		# {"feature": "Occupation", "instances": 31, "metric_value": 0.9812, "depth": 2}
		if obj[3]<=6:
			# {"feature": "Passanger", "instances": 17, "metric_value": 0.9774, "depth": 3}
			if obj[0]>0:
				# {"feature": "Coupon", "instances": 16, "metric_value": 0.9544, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[2]>0:
						# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[6]>2:
							return 'False'
						else: return 'False'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[1]>3:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[6]>1:
						# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[2]<=1:
							return 'True'
						elif obj[2]>1:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[6]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		elif obj[3]>6:
			# {"feature": "Coupon", "instances": 14, "metric_value": 0.7496, "depth": 3}
			if obj[1]>0:
				# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Passanger", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[0]>1:
						# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=2:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[0]<=1:
						return 'True'
					else: return 'True'
				elif obj[2]>3:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[4]>2.0:
		return 'False'
	else: return 'False'

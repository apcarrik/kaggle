def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[1]>0:
		# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.9183, "depth": 2}
		if obj[4]<=2.0:
			# {"feature": "Education", "instances": 28, "metric_value": 0.9403, "depth": 3}
			if obj[2]>0:
				# {"feature": "Direction_same", "instances": 19, "metric_value": 0.9819, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Distance", "instances": 18, "metric_value": 0.9911, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Passanger", "instances": 17, "metric_value": 0.9975, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[3]>1:
								return 'False'
							elif obj[3]<=1:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[3]>1:
								return 'True'
							elif obj[3]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]>2:
						return 'True'
					else: return 'True'
				elif obj[5]>0:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[3]<=15:
					# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[5]>0:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[6]<=2:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[5]<=0:
						return 'True'
					else: return 'True'
				elif obj[3]>15:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]>2.0:
			return 'True'
		else: return 'True'
	elif obj[1]<=0:
		# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 2}
		if obj[0]<=1:
			return 'False'
		elif obj[0]>1:
			return 'True'
		else: return 'True'
	else: return 'False'

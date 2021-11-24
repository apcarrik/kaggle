def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[2]>1:
		# {"feature": "Distance", "instances": 21, "metric_value": 0.9587, "depth": 2}
		if obj[7]<=2:
			# {"feature": "Coupon", "instances": 17, "metric_value": 0.874, "depth": 3}
			if obj[1]>2:
				# {"feature": "Passanger", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Direction_same", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[6]<=0:
						return 'False'
					elif obj[6]>0:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[5]>0.0:
							return 'True'
						elif obj[5]<=0.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			elif obj[1]<=2:
				return 'False'
			else: return 'False'
		elif obj[7]>2:
			# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]>4:
					return 'False'
				elif obj[3]<=4:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Occupation", "instances": 13, "metric_value": 0.3912, "depth": 2}
		if obj[3]>0:
			return 'True'
		elif obj[3]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'

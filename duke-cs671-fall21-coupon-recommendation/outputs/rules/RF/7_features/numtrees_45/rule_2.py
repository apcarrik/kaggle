def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Distance", "instances": 16, "metric_value": 1.0, "depth": 2}
		if obj[6]>1:
			# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[4]>1.0:
				return 'False'
			elif obj[4]<=1.0:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>2:
					# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]<=4:
						return 'False'
					elif obj[3]>4:
						return 'True'
					else: return 'True'
				elif obj[1]<=2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[6]<=1:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[1]>0:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[3]<=12:
					return 'True'
				elif obj[3]>12:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>2:
		return 'True'
	else: return 'True'

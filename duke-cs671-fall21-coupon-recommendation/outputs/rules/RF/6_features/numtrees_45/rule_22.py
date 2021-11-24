def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[4]<=1.0:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 2}
		if obj[3]>4:
			# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[0]>1:
				# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2]>0:
					return 'False'
				elif obj[2]<=0:
					# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=2:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]<=1:
				return 'True'
			else: return 'True'
		elif obj[3]<=4:
			return 'False'
		else: return 'False'
	elif obj[4]>1.0:
		# {"feature": "Coupon", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Distance", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[5]<=2:
				return 'True'
			elif obj[5]>2:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=0:
					return 'False'
				elif obj[2]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]>3:
			return 'False'
		else: return 'False'
	else: return 'True'

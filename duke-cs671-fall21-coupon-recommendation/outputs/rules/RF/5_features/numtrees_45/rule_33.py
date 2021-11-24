def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coupon", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[0]>0:
			# {"feature": "Education", "instances": 17, "metric_value": 0.9774, "depth": 3}
			if obj[1]>0:
				# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[3]>0.0:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[3]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[4]>1:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[3]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[4]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[2]<=1:
		return 'True'
	else: return 'True'

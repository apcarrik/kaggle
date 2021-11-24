def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[3]>1:
			# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.8524, "depth": 3}
			if obj[4]>0.0:
				# {"feature": "Coupon", "instances": 16, "metric_value": 0.6962, "depth": 4}
				if obj[1]>1:
					# {"feature": "Distance", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[5]>1:
						return 'False'
					elif obj[5]<=1:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[1]<=1:
					# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[5]>1:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=1:
							return 'True'
						else: return 'True'
					elif obj[5]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[4]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[3]<=1:
			return 'True'
		else: return 'True'
	elif obj[2]>3:
		return 'True'
	else: return 'True'

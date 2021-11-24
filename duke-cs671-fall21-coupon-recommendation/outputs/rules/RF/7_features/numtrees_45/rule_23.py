def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Occupation", "instances": 15, "metric_value": 0.971, "depth": 2}
		if obj[3]>5:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[1]>2:
				# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[2]<=3:
					return 'False'
				elif obj[2]>3:
					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]>1.0:
						return 'False'
					elif obj[4]<=1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[1]<=2:
				# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]>0.0:
						return 'True'
					elif obj[4]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]<=5:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[1]>0:
			return 'True'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[3]>5:
				return 'True'
			elif obj[3]<=5:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Coupon", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Time", "instances": 14, "metric_value": 0.5917, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[4]<=6:
					# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]>0.0:
						return 'True'
					elif obj[5]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[4]>6:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]>3:
			# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[1]<=0:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[1]>0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 2}
		if obj[2]<=3:
			return 'True'
		elif obj[2]>3:
			return 'False'
		else: return 'False'
	else: return 'True'

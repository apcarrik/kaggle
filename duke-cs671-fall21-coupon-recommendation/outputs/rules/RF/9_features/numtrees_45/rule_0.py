def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[4]<=6:
		# {"feature": "Coupon", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[2]<=3:
			return 'True'
		elif obj[2]>3:
			# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[1]<=0:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]>1:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]<=2:
						return 'False'
					elif obj[3]>2:
						return 'True'
					else: return 'True'
				elif obj[0]<=1:
					return 'True'
				else: return 'True'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[4]>6:
		# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[6]>-1.0:
			# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[1]<=3:
				return 'False'
			elif obj[1]>3:
				# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[5]>0.0:
					return 'False'
				elif obj[5]<=0.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]<=-1.0:
			return 'True'
		else: return 'True'
	else: return 'False'

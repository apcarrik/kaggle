def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[4]<=9:
		# {"feature": "Passanger", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[0]>0:
			# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[6]>1.0:
				# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[2]>1:
					# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[5]<=2.0:
						return 'True'
					elif obj[5]>2.0:
						return 'False'
					else: return 'False'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			elif obj[6]<=1.0:
				# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[1]<=2:
					return 'False'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	elif obj[4]>9:
		return 'False'
	else: return 'False'

def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[5]<=1.0:
		# {"feature": "Coupon", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[1]<=3:
			return 'True'
		elif obj[1]>3:
			# {"feature": "Bar", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[4]<=1.0:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[0]>0:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]>0:
						# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]<=4:
							return 'True'
						elif obj[3]>4:
							return 'False'
						else: return 'False'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[4]>1.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[5]>1.0:
		# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 2}
		if obj[0]<=1:
			return 'False'
		elif obj[0]>1:
			# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'

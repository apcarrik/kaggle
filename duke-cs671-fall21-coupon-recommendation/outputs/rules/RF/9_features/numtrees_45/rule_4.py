def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[6]>0.0:
		# {"feature": "Direction_same", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[7]<=0:
			# {"feature": "Passanger", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[0]>1:
				# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[4]>1:
					return 'True'
				elif obj[4]<=1:
					return 'False'
				else: return 'False'
			elif obj[0]<=1:
				# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=0:
					# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]>0.0:
						return 'True'
					elif obj[5]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[3]>0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[7]>0:
			return 'True'
		else: return 'True'
	elif obj[6]<=0.0:
		return 'False'
	else: return 'False'

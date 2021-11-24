def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[4]<=10:
		# {"feature": "Bar", "instances": 19, "metric_value": 0.6292, "depth": 2}
		if obj[5]<=2.0:
			# {"feature": "Coupon", "instances": 18, "metric_value": 0.5033, "depth": 3}
			if obj[2]>0:
				return 'True'
			elif obj[2]<=0:
				# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=3:
						return 'False'
					elif obj[3]>3:
						return 'True'
					else: return 'True'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[5]>2.0:
			return 'False'
		else: return 'False'
	elif obj[4]>10:
		return 'False'
	else: return 'False'

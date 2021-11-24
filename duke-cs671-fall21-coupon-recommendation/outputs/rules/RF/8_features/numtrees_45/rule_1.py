def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[5]<=1.0:
		return 'True'
	elif obj[5]>1.0:
		# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]>6:
						# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]>0.0:
							return 'True'
						elif obj[4]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[3]<=6:
						return 'True'
					else: return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[2]>2:
			return 'False'
		else: return 'False'
	else: return 'False'

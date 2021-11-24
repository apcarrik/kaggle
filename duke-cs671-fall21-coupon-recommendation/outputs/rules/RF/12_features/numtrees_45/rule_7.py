def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[6]<=7:
		# {"feature": "Education", "instances": 14, "metric_value": 1.0, "depth": 2}
		if obj[5]>0:
			# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[8]<=3.0:
				# {"feature": "Bar", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[7]>-1.0:
					return 'False'
				elif obj[7]<=-1.0:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=1:
						return 'True'
					elif obj[1]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[8]>3.0:
				return 'True'
			else: return 'True'
		elif obj[5]<=0:
			return 'True'
		else: return 'True'
	elif obj[6]>7:
		return 'True'
	else: return 'True'

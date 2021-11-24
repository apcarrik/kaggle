def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[9]>1:
		# {"feature": "Occupation", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[4]<=9:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[2]<=3:
				return 'False'
			elif obj[2]>3:
				# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]>-1.0:
						return 'False'
					elif obj[5]<=-1.0:
						return 'True'
					else: return 'True'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]>9:
			return 'True'
		else: return 'True'
	elif obj[9]<=1:
		# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[4]<=10:
			return 'True'
		elif obj[4]>10:
			return 'False'
		else: return 'False'
	else: return 'True'

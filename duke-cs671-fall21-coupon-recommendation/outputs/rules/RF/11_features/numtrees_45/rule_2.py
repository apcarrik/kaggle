def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]<=1:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[5]>5:
			# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[8]<=1.0:
				# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[6]>1.0:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=0:
						return 'True'
					elif obj[4]>0:
						return 'False'
					else: return 'False'
				elif obj[6]<=1.0:
					return 'False'
				else: return 'False'
			elif obj[8]>1.0:
				return 'True'
			else: return 'True'
		elif obj[5]<=5:
			return 'False'
		else: return 'False'
	elif obj[1]>1:
		return 'True'
	else: return 'True'

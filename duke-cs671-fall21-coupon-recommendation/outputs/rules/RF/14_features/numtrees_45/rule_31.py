def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[4]<=4:
		# {"feature": "Time", "instances": 18, "metric_value": 1.0, "depth": 2}
		if obj[1]>0:
			# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[11]<=1.0:
				# {"feature": "Children", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[5]<=0:
					return 'False'
				elif obj[5]>0:
					# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[9]>0.0:
						return 'False'
					elif obj[9]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[11]>1.0:
				# {"feature": "Children", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[5]<=0:
					return 'True'
				elif obj[5]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[4]>4:
		return 'False'
	else: return 'False'

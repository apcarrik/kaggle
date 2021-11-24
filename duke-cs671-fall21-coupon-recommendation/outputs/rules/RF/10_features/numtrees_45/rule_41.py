def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[5]<=0.0:
		# {"feature": "Education", "instances": 13, "metric_value": 0.9612, "depth": 2}
		if obj[3]<=3:
			# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 3}
			if obj[7]>0.0:
				# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2]<=3:
						return 'True'
					elif obj[2]>3:
						return 'False'
					else: return 'False'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			elif obj[7]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[3]>3:
			return 'True'
		else: return 'True'
	elif obj[5]>0.0:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[4]>7:
			# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[7]>1.0:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=2:
					return 'False'
				elif obj[2]>2:
					return 'True'
				else: return 'True'
			elif obj[7]<=1.0:
				return 'True'
			else: return 'True'
		elif obj[4]<=7:
			return 'True'
		else: return 'True'
	else: return 'True'

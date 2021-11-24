def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Gender", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[4]>0:
		# {"feature": "Coupon", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[2]>2:
			# {"feature": "Age", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[5]<=3:
				# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[8]>1:
					return 'True'
				elif obj[8]<=1:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[7]<=0:
						return 'False'
					elif obj[7]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]>3:
				# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]<=0:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0]>0:
						return 'True'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				elif obj[3]>0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]<=2:
			return 'True'
		else: return 'True'
	elif obj[4]<=0:
		# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 2}
		if obj[0]<=2:
			return 'False'
		elif obj[0]>2:
			# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'

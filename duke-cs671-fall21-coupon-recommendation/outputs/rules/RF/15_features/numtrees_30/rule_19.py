def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.8338, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Coupon_validity", "instances": 18, "metric_value": 0.9911, "depth": 2}
		if obj[3]<=0:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[8]>1:
				return 'True'
			elif obj[8]<=1:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>3:
					return 'True'
				elif obj[1]<=3:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]>0:
			# {"feature": "Age", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[5]>1:
				return 'False'
			elif obj[5]<=1:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[7]<=1:
					return 'True'
				elif obj[7]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.3373, "depth": 2}
		if obj[12]<=2.0:
			return 'True'
		elif obj[12]>2.0:
			# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]>2:
				return 'True'
			elif obj[2]<=2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'

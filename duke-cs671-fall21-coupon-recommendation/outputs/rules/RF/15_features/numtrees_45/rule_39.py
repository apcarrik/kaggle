def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Age", "instances": 18, "metric_value": 0.9911, "depth": 2}
		if obj[5]>0:
			# {"feature": "Income", "instances": 15, "metric_value": 0.9183, "depth": 3}
			if obj[9]<=5:
				# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[7]>0:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[8]<=10:
						return 'True'
					elif obj[8]>10:
						return 'False'
					else: return 'False'
				elif obj[7]<=0:
					return 'False'
				else: return 'False'
			elif obj[9]>5:
				return 'False'
			else: return 'False'
		elif obj[5]<=0:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
